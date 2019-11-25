import random


def read(file):
    f = open(file, "r")
    for i in f.readlines():
        print(i)
    f.close()


def check(name, file):
    f = open(file, "r")
    for i in f.readlines():
        if name in i:
            print("Esiste già!")
            return True
    f.close()
    return False


def write(name, file):
    f = open(file, "a")
    if check(name):
        print("Impossibile modificare")
    else:
        f.write(name + "\n")
    f.close()


def giveList(file):
    f = open(file, "r")
    temp = []
    for i in f.readlines():
        if "--" not in i:
            temp.append(i.replace("\n", ""))
    f.close()
    return temp


def giveJustOne(file):
    f = open(file, "r")
    temp = []
    for i in f.readlines():
        if "--" not in i:
            temp.append(i.replace("\n", ""))
    f.close()
    return temp[random.randint(0, len(temp) - 1)]
