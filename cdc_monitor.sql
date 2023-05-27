USE [master]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER PROCEDURE [dbo].[usp_cdc_hadr_watch_status]
AS 
BEGIN
    SET NOCOUNT ON

    DECLARE @database_name nvarchar(255)
    DECLARE @SQL nvarchar(MAX)

    DECLARE cdc_watch_status_dbs CURSOR FAST_FORWARD READ_ONLY
    FOR
    SELECT [name] FROM sys.databases WHERE [is_cdc_enabled] = 1

    OPEN cdc_watch_status_dbs

    FETCH NEXT FROM cdc_watch_status_dbs INTO @database_name

    WHILE @FETCH_STATUS = 0
    BEGIN

        SET @SQL = 'USE [' + @database_name + '];
DECLARE @job_id_capture uniqueidentifier
DECLARE @job_owner_capture sysname
DECLARE @job_name_capture nvarchar(255)
DECLARE @job_id_cleanup uniqueidentifier
DECLARE @job_name_cleanup nvarchar(255)
DECLARE @msg varchar(max)
DECLARE @dbname varchar(max)
SELECT @dbname = DB_NAME()

IF OBJECT_ID(''tempdb..#cdc_job'') IS NOT NULL
EXEC (''DROP TABLE #cdc_job'')
IF OBJECT_ID(''tempdb..#cdc_job_detail'') IS NOT NULL
EXEC (''DROP TABLE #cdc_job_detail'')

CREATE TABLE #cdc_job(job_id uniqueidentifier,
job_type char(8),
job_name nvarchar(255),
maxtrans smallint,
maxscans smallint,
continuous bit,
pollinginterval smallint,
[retention] smallint,
threshold smallint)
INSERT INTO #cdc_ob
EXEC sys.sp_cdc_help_jobs

SELECT @job_owner_capture = sp.name, @job_id_capture = sj.job_id, @job_name_capture = cj.job_name
FROM #cdc_job AS cj
JOIN msdb.dbo.sysjob AS sj ON sj.name = cj.job_name
JOIN sys.server_principals AS sp ON sp.sid = sj.owner_sid
WHERE cj.job_type = ''capture''

SELECT @job_id_cleanup = cj.job_id, @job_name_cleanup = cj.job_name
FROM #cdc_job AS cj
WHERE cj.job_type = ''cleanup''

IF @job_id_capture IS NULL
SELECT ''sqlserver.sqlserver.customquery.CDCJobCheck'' AS [metric], ''gauge'' AS [type], 1 AS [value], ''dbname: '' + @dbname + ''; error: CDC capture job is not found'' AS [tags]

IF @job_id_capture IS NULL
SELECT ''sqlserver.sqlserver.customquery.CDCJobCheck'' AS [metric], ''gauge'' AS [type], 2 AS [value], ''dbname: '' + @dbname + ''; error: CDC capture job is not found'' AS [tags]

IF @job_id_capture IS NOT NULL
BEGIN
CREATE TABLE #cdc_job_detail(job_id uniqueidentifier NOT NULL,
last_run_date int NOT NULL,
last_run_time int NOT NULL,
next_run_date int NOT NULL,
next_run_time int NOT NULL,
next_run_schedule_id int NOT NULL
requested_to_run int NOT NULL,
request_source int NOT NULL
request_source_id sysname COLLATE database_default NULL,
running int NOT NULL,
current_step int NOT NULL,
current_retry_attempt int NOT NULL,
job_state int NOT NULL)

INSERT INTO #cdc_job detail
EXEC master.dbo.xp_sqlagent_enum_jobs 0, @job_owner_capture

-- Check capture job is disabled
IF (SELECT [enable] FROM msdb.dbo.sysjobs WHERE job_id = @job_id_capture) = 0
SELECT ''sqlserver.sqlserver.customquery.CDCJobCheck'' AS [metric], ''gauge'' AS [type], 3 AS [value], ''dbname: '' + ''; jobname: '' + @job_name_capture + ''; error: CDC Capture job is currently disable'' AS [tags]
ELSE
BEGIN

-- Check capture job status
IF (SELECT [enabled] FROM msdb.dbo.sysjobs WHERE job_id = @job_id_capture) != 1
BEGIN
DECLARE @err VARCHAR(max)
SET @err = (SELECT TOP 1 error_number FROM sys.dm_cdc_errors)

IF @err IS NOT NULL
SET @err = (SELECT TOP 2 error_message AS [text()] FROM sys.dm_cdc_errors FOR XML PATH (''''))
ELSE
SET @err = ''CDC Capture job is not running''

SELECT ''sqlserver.sqlserver.customquery.CDCJobCheck'' AS [metric], ''gauge'' AS [type], 5 AS [value], ''dbname: '' + @dbname + ''; jobname: '' + @job_name_capture + ''; error: '' + @err AS [tags]
END

-- Check cleanup job is disabled
IF (SELECT [enabled] FROM msdb.dbo.sysjobs WHERE job_id = @job_id_cleanup) = 0
SELECT ''sqlserver.sqlserver.customquery.CDCJobCheck'' AS [metric], ''gauge'' AS [type], 4 AS [value], ''dbname: '' + @dbname + ''; jobname: '' + @job_name_cleanup + ''; error: CDC Cleanup job is currently disabled'' AS [tags]
END
END'

        EXEC (@SQL)
        FETCH NEXT FROM cdc_watch_status_dbs INTO @database_name
    END

    CLOSE cdc_watch_status_dbs
    DEALLOCATE cdc_watch_status_dbs
END
GO

-- Initialize Variables
DECLARE @database_name nvarchar(255)
DECLARE @command varchar(max)
DECLARE @chvUser varchar(50) = CAST(SERVERPROPERTY('ServerName') AS varchar) + '\ddagentuser'

SET @command = 'USE [master];
GRANT EXECUTE ON OBJECT::[dbo].[usp_cdc_hadr_watch_status] TO [' + @chvUser + ']
GRANT EXECUTE ON OBJECT::[dbo].[usp_cdc_hadr_watch_status] TO [public]

GRANT EXECUTE ON [sys].[xp_sqlagent_enum_jobs] TO [' + @chvUser + ']
GRANT EXECUTE ON [sys].[xp_sqlagent_enum_jobs] TO [public]'

EXEC (@command)

-- Grant DB Owner role
-- Separate powershell script

DECLARE cdc_grant_db_owner CURSOR FAST FAST_FORWARD READ_ONLY
FOR
SELECT [name] FROM sys.databases WHERE [is_cdc_enabled] = 1

OPEN cdc_grant_db_owner
FETCH NEXT FROM cdc_grant_db_owner INTO @database_name

WHILE @@FETCH_STATUS = 0
BEGIN
    SET @command = 'USE [' + @database_name + '];
ALTER ROLE [db_owner] ADD MEMBER [' + @chvUser + ']';
EXEC (@command)
FETCH NEXT FROM cdc_grant_db_owner INTO @database_name
END

CLOSE cdc_grant_db_owner
DEALLOCATE cdc_grant_db_owner