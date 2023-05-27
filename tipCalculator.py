print("Welcome to the tip calculator.")
bill = input("What was the total bill? ")
percent = input("What percentage tup would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

bill_x_percent = int(bill) * ((float(percent) / 100))
bill_add_bp = int(bill) + bill_x_percent

tip = round(bill_add_bp / int(people))
print(f"Each will receive a {tip} tip")