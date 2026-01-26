class User:

    # 1 створити конструктор з параметрами - імя, вік, почта
    # 2 @property email  та setter з перевіркою @
    def speak(self):
        print(f"{self.name} - i can speak!")


user1 = User()

user1.name = "Max"
print(user1.name)
user1.speak()

user2 = User()
user2.speak()
# user2.name = "Max"
user2.age = 20
print(user2.name)
print(user2.age)


class BankAccount:
    status = 'created'

    def __init__(self, name, balance):
        # public prop
        self.name = name
        # private prop
        self.__balance = balance
        # protected prop
        self._id = 1

    def showInfo(self):
        return f"User {self.name} with balance = {self.__balance}\nstatus: {BankAccount.status}"

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance < 0")
        self.__balance = new_balance


card1 = BankAccount('Max', 100000)
card2 = BankAccount('Ilon', 10)
BankAccount.status = "closed"
# card1.__balance = -1000
print(card1.showInfo())
print(card2.showInfo())

card1.balance = -444
print(card1.balance)



