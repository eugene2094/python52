class Animal:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def getInfo(self):
        return f"Name: {self.name}, age: {self._age}"

    @classmethod
    def createAnimal(cls, name, year):
        return cls.__init__()


