from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise Exception
        self._age = age

    @abstractmethod
    def speak(self):
        pass

obj = Animal("test",12)


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print("gav gav")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.hp = 9

    def __str__(self):
        return super().__str__() + f" hp: {self.hp}"

    def speak(self):
        print("mau mau")


class Caw(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.milk = 0

    def __str__(self):
        return super().__str__() + f" milk: {self.milk}"

    def speak(self):
        print("mu mu")


# cat, caw

dog1 = Dog("Sharik", 5)
# print(dog1)
# dog1.age = 3
# print(dog1.age)
#
cat1 = Cat('barsik', 10)
caw1 = Caw('Burenka', 3)


class Zoo:
    def __init__(self):
        self.animals = []

    def add_new_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)

    def show_animals(self):
        print("Animals in zoo:")
        for animal in self.animals:
            print(animal)
            animal.speak()


zoo = Zoo()
zoo.add_new_animal(cat1)
zoo.add_new_animal(dog1)
zoo.add_new_animal("caw1")

zoo.show_animals()


class BasicC:
    _spec = "main"

    def showSpec(self):
        print(BasicC._spec)


class Child(BasicC):
    print(BasicC._spec)


obj = Child()
obj.showSpec()


class Engine:
    def start(self):
        print("Engine start!")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()


car1 = Car()
car1.start()
