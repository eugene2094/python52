number = 10
print(number + 10)

# list

user_numbers = [1, 2, 3, 4, 5]
print(user_numbers)
print(type(user_numbers))

students = ['Djon', "Bill", "Max"]
print(f"students: {students}")

mix_items_list = ['qwerty', 1, 1, 1, 2, 4.5, True, [3, 4, 5]]
print(mix_items_list)

empty_list = []
print(empty_list)

newList = list((1, 2, 3))
print(newList)

text = "10 20 30 40 50"
list_from_str = text.split()
print(list_from_str)

for i in range(10):
    print(i)

nums_from_for = [i * i for i in range(10)]
print(nums_from_for)

import random

rand_nums = [random.randint(-10, 10) for i in range(10)]
print(f"rand nums: {rand_nums}")

print(f"first st in list: {students[0]}")
print(f"second st in list: {students[1]}")
print(f"last st in list: {students[-1]}")
print(f"Count of elem {len(rand_nums)}")

print(list_from_str[0:3])
print(list_from_str[:2])
print(list_from_str[::-1])

for elem in students:
    print(elem)

for num in rand_nums:
    print(num, end=' ')

print()
marks = [9, 2, 10, 11]
print(f"old marks: {marks}")
# update elem in list
index = 1
if index >= 0 and index < len(marks):
    marks[index] = 10
print(f"updated marks: {marks}")

# list methods
# add new elem
students = ['Djon', "Bill", "Max"]

students.append("Nick")
students.insert(0, 'James')
print(students)
print(f"len {len(students)}")

# del elem in list
students.pop(0)
students.remove("Bill")
print(students)
print(f"len {len(students)}")
if 'Max' in students:
    print(students.index('Max'))

new_sts = ['Tom', 'Kevin']
students.extend(new_sts)
print(students)
students.sort()
print(students)

# rand_nums.sort()
print(rand_nums)

print(max(rand_nums))
print(min(rand_nums))
print(sum(rand_nums))
print(sorted(rand_nums))

#
# Завдання 1
# Користувач з клавіатури вводить елементи списку цілих. Необхідно порахувати суму всіх елементів та їхнє середньоарифметичне.
# # Результати вивести на екран.
#
# user_num = -1
# nums = []
# while user_num != 0:
#     user_num = int(input("Enter num - "))
#     nums.append(user_num)
#
# print(nums)
# print(f"Sum of nums: {sum(nums)}")
# print(f"Avg of nums: {sum(nums) / (len(nums) - 1)}")

# Завдання 2
# Користувач з клавіатури вводить елементи списку цілих і деяке число. Необхідно порахувати скільки разів дане число присутнє у списку.
# Результат вивести на екран.

user_num = -1
nums = []
while user_num != 0:
    user_num = int(input("Enter num - "))
    nums.append(user_num)

find_num = int(input("What num ? - "))
print(f"Value {find_num} count {nums.count(find_num)}")
#
# Завдання 3
# У списку цілих, заповненому випадковими числами обчислити:
# Суму від'ємних чисел;
# Суму парних чисел;
# Суму непарних чисел;


