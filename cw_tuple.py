# tuple, set, frozenset

userTypes = ('admin', 'student', 'teacher')
print(type(userTypes))
print(userTypes)
# userTypes[0] = 'admin2'

# const var
NUMBER_PI = 3.14
print(NUMBER_PI)

myEmptyTuple = ()
print(type(myEmptyTuple))
tuple1 = (1,)
print(type(tuple1))

tuple2 = tuple([1, 2, 3])
print(tuple2)

itemTuple = ('item1', 'item2', 'item1', 100, 200, 300, (1, 2, 3), [4, 5, 6])
print(itemTuple)
print(itemTuple[0])
print(itemTuple[-1])

# del itemTuple
# print(itemTuple)

print(itemTuple.count('item1'))
for i in range(len(itemTuple)):
    print(itemTuple[i])

for elem in itemTuple:
    print(elem)

tuple3 = tuple1 + tuple2
print(tuple3)


def askPersonInfo():
    fName = input("Enter f name ")
    lName = input("enter l name ")
    yearBirth = input("Enter year birth ")
    return fName, lName, yearBirth


# personalInfo = askPersonInfo()
# print(personalInfo)


# def askHobby():
#     hobbyInd = 1
#     hobbyList = []
#     while True:
#         hobbyName = input("Enter name hobby - ")
#         if hobbyName == "":
#             print("No info.Input stopped !")
#             break
#         else:
#             hobbyList.append(hobbyName)
#             hobbyInd += 1
#     if len(hobbyList) > 0:
#         print(f"You have {hobbyInd - 1} hobbies!")
#     else:
#         print("You have no hobbies!")
#     return hobbyList

def askAdditionalInfo(queryStr):
    infoInd = 1
    infoList = []
    while True:
        infoName = input("Enter name of info - ")
        if infoName == "":
            print("No info.Input stopped !")
            break
        else:
            infoList.append(infoName)
            infoInd += 1
    if len(infoList) > 0:
        if queryStr == 'hobby':
            print(f"You have {infoInd - 1} hobbies!")
        elif queryStr == 'prog lang':
            print(f"You have {infoInd - 1} prog languages!!")
    else:
        print("You have no hobbies!")
    return infoList


# userInfo = []
# userInfo.append(askPersonInfo())
# userInfo.append(askAdditionalInfo('hobby'))

# print(userInfo)

# set

mySet1 = {1, 2, 3, 3}
mySet2 = {'Joe', 'Bob', 'Bill'}
mySet3 = {23, 'test', True, (1, 2)}
print(type(mySet1))
print(mySet1)

nums = [12, 12, 12, 32, 54, 76, 34]
print(set(nums))

myList = ['111', ('222', '333')]
print(set(myList))

marks1 = {8, 9, 8}
marks2 = {9, 8, 8}
print(marks1 == marks2)

for elem in mySet2:
    print(elem)

word = "some letter"

for letter in set(word):
    print(letter)

mySet = {1, 2, 3}
print(mySet)

mySet.add(4)
mySet.update([3, 4, 5])

if 5 in mySet:
    mySet.remove(5)

mySet.discard(4)
mySet.pop()

print(mySet)

oldUsers = {'user1', 'user2', 'user3'}
newUsers = {'user3', 'user4', 'user5'}

print(oldUsers)
print(newUsers)
print("intersection of sets")
print(oldUsers & newUsers)
print(oldUsers.intersection(newUsers))
print("Union of sets")
print(oldUsers | newUsers)
print(oldUsers.union(newUsers))
print("Difference of sets")
print(oldUsers - newUsers)
print(newUsers.difference(oldUsers))

# frozenset()
frozenA = frozenset(oldUsers)
print(frozenA)
