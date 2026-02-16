# list / tuple /  set

# create tuple

my_tuple1 = ()
print(type(my_tuple1))
my_tuple2 = tuple([1, 2, 3])
print(my_tuple2)

my_tuple3 = ('one', "two", '123', 4, True, [1, 2, 3], 4)
print(my_tuple3)

print(my_tuple3[0])
print(my_tuple3[-1])
print(f"length: {len(my_tuple3)}")

print(my_tuple3.count(4))
print(my_tuple3.index(4, 5))

nums = (1, 2, 3, 4)
print(nums)

n1, n2, *n3 = nums
print(n1, n2, n3)

for elem in my_tuple3:
    print(elem, end=" | ")

print()

print(my_tuple2 + my_tuple3)


def get_user_info(*args):
    print(args)
    return 'Bob', 30, 'Kiev'


print(type(get_user_info()))
name, age, city = get_user_info()
print(name, age, city)
print(get_user_info())

users = [
    ('Anna', '932453'),
    ('Max', "12312321")
]

for name, phone in users:
    print(f"Name: {name}, phone: {phone}")

# my_tuple3[0] = 1  # TypeError: 'tuple' object does not support item assignment

t = (1,)
print(type(t))


def process_order(price, is_premium):
    bonus = 0
    status = 'processed'
    if is_premium:
        bonus = price * 0.1
        final_price = price * 0.9

    else:
        final_price = price

    return final_price, bonus, status


result = process_order(100, True)
print(result)

final_price, bonus, status = process_order(100, True)

print(f"price: {final_price}\nbonus: {bonus}\nstatus: {status}")

# set()

set1 = {1, 2, 3}
set2 = {'Bob', 'Bill', 'Max'}
set3 = {23, 'Nick', 3.14, True, (1, 2, 3)}

print(set1)
print(set2)
print(set3)
print(type(set3))

set4 = set((10, 20, 30))
print(set4)

uniqueUsers = {'Bill', 'Bob', 'Joe', 'Bill'}
print(uniqueUsers)

setA = {1, 3, 2}
setB = {3, 2, 1}
print(setA == setB)

setA.add(4)
setA.update([5, 6, 7])

setA.remove(4)
setA.discard(1)
print(setA)
setA.pop()
print(setA.pop())
print(setA)

products1 = {'iphone11', 'iphone12', 'iphone13'}
products2 = {'iphone13', 'iphone14', 'iphone15'}

print(f"products1: {products1}")
print(f"products2: {products2}")

print("----------------Intersection---------------")
print(products1.intersection(products2))
print(products1 & products2)

print("----------------Union---------------")
print(products1.union(products2))
print(products1 | products2)

print("----------------Difference---------------")
print(products1.difference(products2))
print(products2 - products1)

fset = frozenset(setA)
print(type(fset))

allPizzaTypes = ['Margarita', '4Cheese', 'Franchesko', 'Meat', 'Carbonara', 'Margarita']

uniquePizzaTypes = list(set(allPizzaTypes))
print(allPizzaTypes)
print(uniquePizzaTypes)

userApp1 = ['user123', 'qwerty6', 'admin4', 'student3']
userApp2 = ['user123', 'qwerty5', 'admin4', 'student6']

print("users1 + users2")
print(set(userApp1) | set(userApp2))
print(set(userApp1) & set(userApp2))
print(set(userApp1) - set(userApp2))


