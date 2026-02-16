# bool - True / False
# >, <, >=, <=, ==, !=

print(f"1 > 10 = {1 > 10}")
print(f"1 < 10 = {1 < 10}")
print(f"1 >= 10 = {10 >= 10}")
print(f"1 != 0 = {1 != 0}")

print(bool("qwe"))
print(bool(0))
print(bool(100))

# if else
# car_speed = int(input("Enter car speed - "))
#
# if car_speed > 60:
#     # body if
#     print("Speed to high !")
# else:
#     # body else
#     print("Speed is normal !")
#
# # and or  not
#
# if car_speed > 0 and car_speed < 60:
#     print("Speed is normal!")
#
# if 0 < car_speed < 60:
#     print("Speed is normal!")
#
# year = 2003
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f"Year {year} is leap!")
# else:
#     print(f"Year {year} is no leap!")
#
# print(not True)
# print(not False)
#
# password = "admin"
# user_password = input("Enter pass ")
# if user_password == password:
#     print("Welcome !")
# else:
#     print("Error password !")

# elif
temp = 40

if -15 < temp < 50:
    if temp > 35:
        print("Temp is very hot !")
    elif temp > 15:
        print("Temp is warm !")
    elif temp > 0:
        print("Temp is cold !")
else:
    print("error temp !")

score = 0
print("Math victorins !")
ans1 = float(input("Question 1: 2+2 = ?"))
if ans1 == 4:
    print("Cool ! You are right ! Go next !")
    score += 1
    print(f"Your score is {score}")
else:
    print("Not right !")

ans1 = float(input("Question 1: 2*2 = ?"))
if ans1 == 4:
    print("Cool ! You are right ! Go next !")
    score += 1
    print(f"Your score is {score}")
else:
    print("Not right !")

if score == 2:
    print("Your mark is 12")
elif score == 1:
    print("Your score is 10")
else:
    print("Bad mark ! Try again !")
