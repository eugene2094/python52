import random


def add(x):
    return x + 10


# lambda function
newNum = lambda x: x + 10

nums = [random.randint(1, 100) for i in range(10)]
print(nums)

for num in nums:
    print(add(num))

for num in nums:
    print((lambda x: x + 10)(num))

students = [['Nick', 80], ['Djon', 6], ['Bill', 44], ['Tom', 90]]
print(students)

sortedSts = sorted(students, key=lambda x: x[1])
print(sortedSts)

grnToDollar = 42
discount = 0.15

priceDol = lambda x: x / grnToDollar * (1 - discount)
print(f"price: {priceDol(4200)}")

userName = lambda fName, lName: f"Full users name : {fName.title()} {lName.title()}"
print(userName("bill", "djackson"))

studBirthYear = [2000, 2001, 1997, 1990]
studAges = list(map(lambda year: 2025 - year, studBirthYear))

# for year in studBirthYear:
#     studAges.append(2025 - year)

print(studAges)
login = 'admin'
password = '1111'


def userAction(login, passw, func):
    return func(login, passw)


def showInfo(login, passw):
    print(login, passw)


def changePass(userLog, userPass):
    global login, password
    if userLog.lower() == login and userPass == password:
        newPass = input("Enter new password - ")
        if len(newPass) > 4:
            password = newPass
        else:
            print("Error new password!")


userAction('admin', 'asdfadsf', showInfo)
# userAction('admin', '1111', changePass)

userLogs = ['ADMin', 'STUDENT', 'UGDasdhf', 'User']

userLogsLow = list(map(str.lower, userLogs))
print(userLogsLow)

values = ['2', '34', '6.7', '4.5']
nums = list(map(float, values))
print(nums)

numList1 = [10, 20, 30]
numList2 = [1, 2, 3]

result = list(map(lambda a, b: a ** b, numList1, numList2))
print(result)

# filter
prices = [100, 34, 78, 45, 23, 53]
expensive = list(filter(lambda x: x > 50, prices))
print(expensive)

userLogs = ['ADMin', 'userSTUDENT', 'UGDasdhf', 'User']


def checkLogin(login):
    if login.lower().find('user') != -1:
        return True
    else:
        return False


selectedUser = list(filter(checkLogin, userLogs))
print(selectedUser)

# zip

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd']

print(list(zip(list1, list2)))
#
# numbers = [input("Enter numbers a list :  ") for i in range(5)]
# print(numbers)
# print(f"first nun and count in list : {numbers[0]} {len(numbers)}")

words = input("enter text").split()
print(words)