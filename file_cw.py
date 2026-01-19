import os

try:
    file = open("test.txt", 'w')
    data = "hello from python\n"
    for i in range(5):
        file.write(str(i) + " " + data)
    file.close()
except FileNotFoundError as ex:
    print(ex)

# str_lists = ['a\n', 'b\n', 'c\n']
#
# try:
#     file = open("test.txt", 'w')
#     file.writelines(str_lists)
#     file.close()
# except FileNotFoundError as ex:
#     print(ex)

try:
    file = open("test.txt", 'r')
    data = file.read(15)
    print(data)
    data = file.read(15)
    print(data)

    line1 = file.readline()
    print(line1)
    lines = file.readlines()
    print(lines)
    file.close()
except FileNotFoundError as ex:
    print(ex)

f = open("test.txt", 'a', encoding="utf-8")
f.write("дадали новий рядок")
f.close()

with open('test.txt', 'r', encoding='utf-8') as filein, open('newdata.txt', 'w', encoding='utf-8') as fileout:
    data = filein.read()
    fileout.write(data)


def replaceTextInFile(fileName, oldText, newText):
    with open(fileName, encoding='utf-8') as file:
        data = file.read()
        data = data.replace(oldText, newText)

    with open(fileName, 'w', encoding='utf-8') as file:
        file.write(data)


def readFromFile(fileName):
    with open(fileName, encoding='utf-8') as file:
        print(file.encoding)
        data = file.read()
        print(data)


try:
    replaceTextInFile('test.txt', '0 hello from python', 'python')
    readFromFile('test.txt')
except:
    pass


def wordCounter(fileName):
    nWords = 0
    with open(fileName, encoding='utf-8') as file:
        data = file.read()
        words = data.split()
        for word in words:
            if not word.isnumeric():
                nWords += 1
    return nWords


print(wordCounter('test.txt'))
