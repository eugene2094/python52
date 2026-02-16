num1 = 2
num2 = 5.7
print(num1 + num2)

str1 = "hello "
str2 = "friends!"
print(str1 + str2)

print([1, 2, 3])


class Book:
    __slots__ = ('title', 'pages')

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def show_info(self):
        print(f"Title: {self.title},pages: {self.pages}")

    def __gt__(self, other):
        if not isinstance(other, Book):
            raise TypeError
        return self.pages > other.pages

    def __eq__(self, other):
        return self.pages == other.pages and self.title == other.title

    def __str__(self):
        return f"Title: {self.title},pages: {self.pages}"

    def __len__(self):
        return self.pages


class Film:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def show_info(self):
        print(f"Title: {self.title},genre: {self.genre}")


film1 = Film("Titanic", 'Drama')
book1 = Book("Python", 500)
book2 = Book("Python 2", 700)

for item in (film1, book1):
    item.show_info()

print(book1 > book2)
print(book1 == book2)
print(book1)

print(len(book1))


class Point:
    def __init__(self, x=0, y=0):
        print("Initialisation of new point")
        self.x = x
        self.y = y

    def __new__(cls, *args, **kwargs):
        print("Creating new point")
        return super().__new__(cls)

    def __str__(self):
        return f"x: {self.x} y: {self.y}"

    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        elif isinstance(other, (int, float)):
            return Point(self.x * other, self.y * other)

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.x += other
            self.y += other
            return self
        elif isinstance(other, Point):
            self.x += other.x
            self.y += other.y
            return self

    def __float__(self):
        return Point(float(self.x), float(self.y))


p1 = Point(2, 2)
p2 = Point(2, 2)
print(p1 * p2)
print(p1 * 3.5)

p1 += p2
print(p1)
print(p2)

print(p1.__float__())
# print(float(p1))

b1 = Book("itstep", 123)


# b1.date = "04.02"

# print(b1.__dict__)


class Base:
    __slots__ = ('a', 'b''c', 'd')


class Child(Base):
    __slots__ = ('e',)


c1 = Child()

c1.a = 1
c1.e = 2
c1.d = 3
