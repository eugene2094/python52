def simpleDecorator(func):
    print("Hello ! i am 1 decorator!")

    def wrapper():
        print("Decorator start working !")
        func()
        print("See you!")

    return wrapper


def simpleDecorator_v2(func):
    print("Hello ! i am 2 decorator!")

    def wrapper():
        print("Decorator start working !")
        func()
        print("See you!")

    return wrapper


# @simpleDecorator
# @simpleDecorator_v2
def sayHi():
    print("Hello!")


# sayHiPro = simpleDecorator(sayHi)

# sayHi()

# sayHiPro()

# newFunc = simpleDecorator(simpleDecorator_v2(sayHi))
# newFunc()


def simpleDecorator_v3(func):
    print("Hello ! i am 3 decorator!")

    def wrapper():
        print("Decorator start working !")
        result = func()
        print("See you!")
        if not result:
            return None

        return result

    return wrapper


# @simpleDecorator_v3
def sum():
    x = 1
    y = 2
    return x + y


# print(sum())
# sumD = simpleDecorator_v3(sum)


def simpleDecorator_v4(func):
    print("Hello ! i am 4 decorator!")

    def wrapper(*args):
        print(args)
        print("Decorator start working !")
        result = func(*args)
        print("See you!")
        if not result:
            return None

        return result

    return wrapper


# @simpleDecorator_v4
def sumNums(n1, n2):
    return n1 + n2


# @simpleDecorator_v4
def sumNums2(n1, n2, n3):
    return n1 + n2 + n3


# print(sumNums(2, 2))
# print(sumNums2(2, 2, 2))


def decoratorWrapper(argForDec):
    print(f"I have got {argForDec} args")

    def simpleDecorator_v5(func):
        print("Hello ! i am 5 decorator!")

        def wrapper(*args):
            print(args)
            print("Decorator start working !")
            result = func(*args)
            print("See you!")
            if not result:
                return None

            return result

        return wrapper

    return simpleDecorator_v5


def calc(a, b):
    return a + b


# decoratorWithArg = decoratorWrapper(10)
# calcSum2 = decoratorWithArg(calc)
# print(calcSum2(2, 2))
#

pricesUsd = [100, 34, 65, 87, 234, 76]
print(pricesUsd)





def setDiscountDecoratorWrapper(discount):
    def changePriceDecoratorWithDesc(function):
        def wrapper(argList):
            print("We have got ", argList, "prices")
            result = function(argList)
            resultWithDesc = list(map(lambda price: price * (1 - discount), result))
            print("Lets set a discount!")
            return resultWithDesc

        return wrapper

    return changePriceDecoratorWithDesc


# changePriceDecor = setDiscountDecoratorWrapper(0.5)
# priceWithDesc = changePriceDecor(toPriceGrn)
# print(priceWithDesc(pricesUsd))

@setDiscountDecoratorWrapper(0.5)
def toPriceGrn(priceList):
    return list(map(lambda x: x * 42, priceList))


print(toPriceGrn(pricesUsd))