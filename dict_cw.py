# dictionary

nums = [1, 2, 3, 4, 5]

student = ['Bob', 23, '+380953454534', 'asdfs@gmail.com']

student_dict = {"name": 'Bob',
                'age': 23,
                'tel': '+380953454534',
                'email': 'asdfs@gmail.com'}

print(student)
print(student_dict)

dict3 = dict(name="Rick", age=20)
print(dict3)

dict4 = dict([('a', 1), ('b', 2)])
print(dict4)

my_dict = {'key1': 1, "key2": 2, "key3": 3}

print(my_dict)
print(my_dict['key3'])

bookInfo = {
    'auther': "Gvido",
    'title': "Python",
    'price': 33,
    'pages': 345
}

# add new pair in dict
bookInfo["lang"] = 'en'

# change value in dict
if 'lang' in bookInfo:
    bookInfo["lang"] = 'du'

print(bookInfo)

for key in bookInfo:
    print(key, ":", bookInfo[key])

for key, value in bookInfo.items():
    print(key, value)

print(bookInfo.values())
print(bookInfo.keys())

print(bookInfo.get('title2'))

bookInfo.update({'qwerty': 123})
print(bookInfo)

bookInfo.pop('qwerty')
print(bookInfo)

# find in dictionary

users = [
    {'name': "Hanna", 'age': 25, 'login': 'qweqe123'},
    {'name': "Mark", 'age': 27, 'login': 'asd123'},
    {'name': "Bob", 'age': 35, 'login': 'stud43'},
    {'name': "Jack", 'age': 45, 'login': 'rockk4'}
]


def find_user(users, keyName, keyValue):
    isElementFound = False
    for user in users:
        if user.get(keyName) == keyValue:
            print("User is found !")
            for key, value in user.items():
                print(f"{key} - {value}")
            isElementFound = True
            break

    if not isElementFound:
        print("Element is not found !")


find_user(users, 'name', 'Bob')
find_user(users, 'age', 35)

print(bookInfo)

sortedBook = sorted(bookInfo.items(), key=lambda x: x[0])
# print(sortedBook)
for elem in sortedBook:
    print(elem[0], elem[1])

sortedUsersByName = sorted(users, key=lambda x: x['name'])
for user in sortedUsersByName:
    print(user)
