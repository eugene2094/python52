class Person1:
    population = 0
    min_age = 18

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.population += 1
        print("Person init")

    def get_info(self):
        return f"My name is {self.name}, age: {self.age}"

    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18

    @staticmethod
    def is_valid_name(name: str) -> bool:
        return name.isalpha() and len(name) >= 2

    def set_name(self, new_name):
        if Person.is_valid_name(new_name):
            self.name = new_name

    @classmethod
    def get_population(cls):
        return cls.population

    @classmethod
    def set_min_age(cls, value):
        cls.min_age = value

    @classmethod
    def from_string(cls, data: str):
        name, age = data.split(",")
        return cls(name.strip(), int(age))


#
# p1 = Person("Anna", 23)
# p2 = Person("Nick", 11)
#
# print(p1.get_info())
# print(Person.is_adult(p1.age))
# print(Person.is_adult(15))
# print(Person.is_valid_name("Qwerty"))
#
# print(f"Population count {Person.get_population()}")
#
# Person.set_min_age(14)
# print(Person.min_age)


class Book:
    def __init__(self, title, auther, pages):
        print("Creating book")
        self.title = title
        self.auther = auther
        self.pages = pages

    def show(self):
        print(f"Title {self.title}\nAuther {self.auther}\npages {self.pages}")


class File:
    def __init__(self, file_size, src):
        print("Creating file")
        self.file_size = file_size
        self.src = src

    def show(self):
        print(f"File size {self.file_size}, src {self.src}")


class EBook(File, Book):
    def __init__(self, title, auther, pages, file_size, src):
        Book.__init__(self, title, auther, pages)
        File.__init__(self, file_size, src)

    def show_ebook(self):
        Book.show(self)
        File.show(self)


# b1 = EBook("Python", "Gvido", 333, 100, "pythonbook.txt")
# b1.show_ebook()
# b1.show()

class Person:
    def __init__(self):
        print("Person init")
        super().__init__()


class Student(Person):
    def __init__(self):
        print("student init")
        super().__init__()

    # def get_info(self):
    #     print(Person.get_info(self) + "I am student")


class Employee(Person):
    def __init__(self):
        print("employee init")
        super().__init__()

    # def get_info(self):
    #     print(Person.get_info(self) + "I am employee")


class WorkingStudent(Student, Employee):
    def __init__(self):
        print("working student init")
        super().__init__()


ws = WorkingStudent()
# ws.get_info()

print(WorkingStudent.mro())
