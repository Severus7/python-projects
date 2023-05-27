import random

letters = ['A', 'B' , 'C' , 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
numLetters = int(input("How many letters would you like in your password?\n"))
numNumbers = int(input("How many number would you like?\n"))
numSymbols = int(input("How many symbols would you like?\n"))

for lenLetters in range(1, numLetters):
    randLetters = random.choices(letters, k=numLetters)
    pwLetters = ''.join(randLetters).lower()

for lenNumbers in range(1, numNumbers):
    randNumbers = random.choices(numbers, k=numNumbers)
    pwNumbers = ''.join(randNumbers).lower()

for lenSymbols in range(1, numSymbols):
    randSymbols = random.choices(symbols, k=numSymbols)
    pwSymbols = ''.join(randSymbols).lower()

password = pwLetters + pwSymbols + pwNumbers

print(password)