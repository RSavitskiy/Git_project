import random


def summ(a, b):
    c = a + b
    return c


def multi(a, b):
    c = a * b
    return c


def string(a, b):
    c = a * b
    return c


def list(a):
    list = [random.randint(0, 10) for x in range(10)]
    for i in list:
        # print(i)
        if i == a:
            print("position " + str(list.index(i)))
            return a


def notEquil(a, b):
    c = a * b
    return c




