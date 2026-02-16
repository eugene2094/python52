# функції

print(list(range(1, 10)))


def say_hello():
    print("func start working!")
    print("hello!")
    print("func finished !")


say_hello()


def say_hi_with_arg(name):
    print(f"hello {name}")


say_hi_with_arg("admin")
say_hi_with_arg("qwerty")


def calculate(num1, num2, num3):
    print("Lets calculate !")
    print(num1 + num2 - num3)


n1 = 1
n2 = 4
calculate(n1, n2, 2)


def changeName(userName):
    newName = userName.upper()
    return newName


name = changeName('student') + "!"
print(changeName("admin"))
print(name)


# if "1".isdigit():

def check_temp(temp):
    if temp > 30:
        return "very hot"
    elif temp > 15:
        return "warm"
    elif temp > 0:
        return "cold"
    else:
        return "very cold"


print(check_temp(40))
print(check_temp(20))

prices = [100, 45, 76, 23]


def convertUSD(list_price):
    result_list = []
    for price in list_price:
        result_list.append(price * 42)
    return result_list


print(convertUSD(prices))


def userGreetings(login, passw="111"):
    if login == 'admin' and passw == 'admin':
        print("Welcome admin")
    elif login == 'student':
        print('Welcome student')
    else:
        print("welcome !")


userGreetings('admin', 'admin')
userGreetings('student')


def sum_nums(n1: int, n2: int, n3=0, n4=0):
    if isinstance(n1, (int, float)):
        return sum([n1, n2, n3, n4])


print(sum_nums(n1=2, n2=2))
print(sum_nums(2.0, 2, 3))


def sum_num_2(*args):
    print(args)
    return sum(args)


print(sum_num_2(2, 2))
print(sum_num_2(2, 2, 2, 2, 2))

# namespace global, local, builin, enclosing
# global
number = 0
global_num = 100


def test_func():
    # local
    global global_num
    func_number = 500
    global_num = -1
    number = 1
    print(f"num func {number}")
    print(f"global num {global_num}")
    print(f"fnc num {func_number}")


print(number)
test_func()

print(number)

# print(f"fnc num {func_number}")
print(global_num)

import random


def out_func():
    num = 100
    random.randint(1, 10)

    def inner_func():
        # nonlocal num
        # num = 200
        print("inner func working with ", num)

    inner_func()


out_func()


def multy(n1, n2):
    return n1 * n2


def minus(n1, n2):
    return n1 - n2


def delete(n1, n2):
    if n2 != 0:
        return n1 / n2
