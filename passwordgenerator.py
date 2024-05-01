#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("THIS IS A RANDOM PASSWORD GENERATOR TOOL")
r_letters = int(input("How many letters would you like in your password?\n")) 
print("total letters in the password you inputted-", r_letters)
r_symbols = int(input("How many symbols would you like?\n"))
print("total symbols in the password you inputted-", r_symbols)
r_numbers = int(input("How many numbers would you like?\n"))
print("total numbers in the password you inputted-", r_numbers)
password_list = []
for char in range(1, r_letters + 1):
  password_list.append(random.choice(letters))
for char in range(1, r_symbols + 1):
  password_list += random.choice(symbols)
for char in range(1, r_numbers + 1):
  password_list += random.choice(numbers)
print(password_list)
random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
  password += char
print(f"Your password is: {password}")