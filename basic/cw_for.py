# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# for i in nums:
# print(i)

num = 0

# for num in 1, 2, 3, 4, 5:
#     print(num)

# for num in range(5):
#     print(num)
#
# print("--------------")
#
# for num in range(1, 6):
#     print(num)
#
# print("--------------")
#
for num in range(1, 10, 2):
    if num == 5:
        break
    print(num)
#
# for s in "python":
#     print(s, end=" - ")
#
# print("---------------------")
#
# for num1 in range(1, 11):
#     for num2 in range(1, 11):
#         print(num1 * num2, end=" | ")
#     print("\n")
#

# while умова:
# дія

# count = 0
#
# while count < 5:
#     print(count)
#     count += 1
#
# user_num = -1
# sum = 0
#
# while user_num != 0:
#     user_num = int(input("Enter num - "))
#     print(f"Your num is: {user_num}")
#     sum += user_num
#
# print(f"Sum of your nums: {sum}")

# break - stop , continue - next iter
#
# while True:
#     num = int(input("Enter num - "))
#     if num == 0:
#         break
#     elif num == 10:
#         break
#     print(num)
#
#
# for num in range(100):
#     if num % 3:
#         continue
#     print(num)
#

floor = 1
energy = 23
print(f"I am on the {floor} floor!")

while floor != 5:
    step = 0
    if floor == 3:
        print("I will take an elevator!")
        break
    while step != 20:
        step += 1
        energy -= 1
        print(f"Step: {step}, energy: {energy}")
        if energy <= 0:
            print("I am tired !Need a rest !")
            energy += 10
    floor += 1
    print(f"I am on the {floor} floor!")


