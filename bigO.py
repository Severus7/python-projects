# O(n) - proportional
# def print_items(n):
#     for i in range(n):
#         print(i)

# print_items(15)

# O(n) Drop Constants (first rule of simplifying)
# def print_items(n):
#     for i in range(n):
#         print(i)

#     for j in range(n):
#         print(j)


# print_items(15)

###########################################################################

# O(n^2) - less efficient from a time complexity standpoint
# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             print(i, j)

# print_items(5)

# Drop non-dominants: O(n^2) + O(n) = O(n^2) because we drop non-dominants
# def print_items(n):
#     # O(n^2)
#     for i in range(n):
#         for j in range(n):
#             print(i, j)

#     # O(n)
#     for k in range(n):
#         print(k)

# print_items(5)

###########################################################################

# O(1) - Constant Time: The number of operations will remain constant as n increases
# O(1) - Most efficient Big(O)
def add_items(n):
    return n + n + n

###########################################################################

# O(log n)