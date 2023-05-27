alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         current_index = alphabet.index(letter)
#         new_index = current_index + shift_amount
#         new_letter = alphabet[new_index]
#         cipher_text += new_letter
#     print(cipher_text)

# def decrypt(encrypted_text, shift_amount):
#     plain_text = ""
#     for letter in encrypted_text:
#         current_index = alphabet.index(letter)
#         new_index = current_index - shift_amount
#         new_letter = alphabet[new_index]
#         plain_text += new_letter
#     print(plain_text)

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(encrypted_text=text, shift_amount=shift)

def caesar(direction, text, shift_amount):
    new_text = ""
    if direction == "decode":
        shift_amount *= -1
    for letter in text:
        current_index = alphabet.index(letter)
        new_index = current_index + shift_amount
        new_text += alphabet[new_index]
    print(new_text)

caesar(direction=direction, text=text, shift_amount=shift)
