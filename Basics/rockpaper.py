import random
import string

letters = string.ascii_letters
digits = string.digits
special_char = string.punctuation

password_list = []
print("Welcome to the pyPassword Generator")
t_letter = int(input("how many letters do you want it in your password?\n"))
t_special = int(input("how mant special characters you want in your password?\n"))
t_digits = int(input("how many digits you want it in your password?\n"))

for i in range(0,t_letter):
    password_list.append(random.choice(letters))

for i in range(0, t_special):
    password_list += random.choice(special_char)

for i in range(0, t_digits):
    password_list += random.choice(digits)

random.shuffle(password_list)
print(password_list)

password = ""
for i in password_list:
    password += i

print("your password is "+password)
