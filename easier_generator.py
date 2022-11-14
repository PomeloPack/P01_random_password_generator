import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Random PyPassword Generator!")


random_number_letters= int(input("How many letters would you like in your password?\n")) 
random_number_numbers = int(input("How many symbols would you like?\n"))
random_number_symbols = int(input("How many numbers would you like?\n"))


# this way choose letter, number and symbol one by one not together random firs will be only letters than numbers and last will be symbols
# example: abc012!#

password = " "

for letter in range(1, random_number_letters + 1):
    password += random.choice(letters)

for number in range(1, random_number_numbers + 1):
    password += random.choice(numbers)

for symbol in range(1, random_number_symbols + 1):
    password += random.choice(symbols)

print(password)
