def sayHello():
    name = input("Enter name - ")
    print(f"hello , {name}")


# sayHello()
#
# num = 100
# print(type(num))
# nums = [1, 2, 3]
#
# print(type(sayHello))
#
# greeting = sayHello
# greeting()

def greetings(customerList, greetFunc):
    for c in customerList:
        greetFunc(c.lower())


def sayHi(customer):
    if customer.find("admin") != -1:
        print(f"Hello, admin - {customer}")
    elif customer.find("student") != -1:
        print(f"Hello, student - {customer}")
    else:
        print(f"Hello, - {customer}")


customerList = ['adminJane', 'ADMINqwerty', 'StudentBill']

greetings(customerList, sayHi)

from cw_func import multy, minus, delete


def userChoice(check):
    if check == '1':
        return multy
    elif check == '2':
        return minus
    elif check == '3':
        return delete


x = 2
y = 3


# for i in range(3):
#     userC = input("Enter choice - ")
#     myCulculation = userChoice(userC)
#     print(myCulculation(x, y))


def factorialCalc(number):
    if number == 0:
        return 1
    else:
        print(f"Number: {number}")
        return number * factorialCalc(
            number - 1)  # 5 * factorialCalc(number - 1) - 5 * 4 * factorialCalc(number - 1) = 5 * 4 * 3 * 2 * 1 * 0


print(factorialCalc(5))


def isStrPalindrom(myStr):
    if len(myStr) == 0:
        return True
    else:
        if myStr[0] == myStr[-1]:
            print(myStr[1:-1])
            return isStrPalindrom(myStr[1:-1])
        else:
            return False


print(isStrPalindrom("level"))


def findMin(numberList):
    if len(numberList) > 1:
        return min(findMin(numberList[:-1]), numberList[-1])
    else:
        return numberList[0]


nums = [2, 4, 1, 8, 3]
print(f"min: {findMin(nums)}")