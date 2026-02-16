from abc import ABC, abstractmethod


class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class PayPal(PaymentSystem):
    def pay(self, amount):
        print("Send money paypal", amount)


class WayForPay(PaymentSystem):
    def pay(self, amount):
        print("Send money wayForPay", amount)


class Crypto(PaymentSystem):

    def pay(self, amount):
        print("Send money crypto", amount)


# pay1 = WayForPay()
# pay1.pay(400)
#
# pay2 = PayPal()
# pay2.pay(200)

obj = Crypto()
print(type(type(obj)))


class Base:
    pass


obj2 = Base()
print(type(type(obj2)))

number = 100
print(type(type(number)))


def method1(self):
    print("test method working !")


NewClass = type('MyClass', (Base,), {'attr1': 100, 'method1': method1})
obj3 = NewClass()
print(obj3.attr1)
obj3.method1()


class MyMetaClass(type):
    def __new__(cls, name, bases, dict):
        # print("Hello from __new__()!")
        # print("Type of the class was created ", cls)
        # print("Name of new class", name)
        # print("List of bases", bases)
        # print("Dict of attr", dict)

        if 'id' not in dict.keys():
            print(f"No 'id' attr in the class {name}")
        else:
            methods = {key: value for key, value in dict.items() if callable(value)}
            if len(methods) > 2:
                print(f"More than 2 methods !")
            else:
                print(f"Class {name} is creating...")
                return super().__new__(cls, name, bases, dict)


class MyClass1(metaclass=MyMetaClass):
    id = 1


class MyClass2(metaclass=MyMetaClass):
    id = 1

    def method1(self):
        pass

    def method2(self):
        pass

    def method3(self):
        pass


print(type(MyClass1))
print(type(MyMetaClass))

obj = MyClass1()
