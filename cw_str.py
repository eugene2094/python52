userMessege = "python"

userMessegeEnc = userMessege.encode('utf-8')
print(userMessegeEnc)
print(userMessege)

userMessegeDec = userMessegeEnc.decode('utf-8')
print(userMessegeDec)

my_str = 'some text'
print(my_str)
print(type(my_str))
print(id(my_str))
my_str = "new   text"
print(id(my_str))

# indexis
print(my_str[0])
print(my_str[1])
print(my_str[-1])
# slices
print(my_str[0:4])
print(my_str[:5])
print(my_str[6:])
print(my_str[:len(my_str) // 2])
print(len(my_str))

# print(my_str[15])

#  +  *
str1 = "first"
str2 = "second"
print(str1 + " " + str2 + str(10))  # concat str
print("2" * 3)

my_str = "new text new"
print(my_str)
print(my_str.lower())
print(my_str.upper())
print(my_str.title())
print(my_str.capitalize())
print(my_str.swapcase())

print(my_str.count('new'))
print(my_str.find('new2'))
# print(my_str.index('new2'))
print(my_str.rfind('new'))

print(my_str.endswith("new"))
print(my_str.startswith("python"))

print(my_str.islower())
print(my_str.isupper())
print(my_str.isdigit())

import string
import random

print(string.digits)
print(string.ascii_letters)
all_symbols = string.digits + string.ascii_letters + string.punctuation
print(all_symbols)

length_pass = int(input("Enter length of pass - "))
password = ""

for i in range(length_pass):
    password += random.choice(all_symbols)

print(password)

check_digit = False
check_lower = False
check_upper = False
check_punctuation = False

if len(password) > 7:
    for s in password:
        if s.isdigit():
            check_digit = True
        elif s.islower():
            check_lower = True
        elif s.isupper():
            check_upper = True
        elif s.isascii():
            check_punctuation = True
else:
    print("Your password to short!")

if check_upper and check_lower and check_digit and check_punctuation:
    print("Password is ok!")
else:
    print("Password not valid !")

