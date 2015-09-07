# find the minimum and maximum value in the leaf (and display their position)
import random

def createList(x):
    list = [random.randint(0, 100) for x in range(x)]
    return list

newList = createList(10)
print(newList)

def maxList(x):
    # assert x
    max = x[0]
    for i in x:
        if i > max:
            max = i
    return max


maxValue = maxList(newList)
print("max value = "+str(maxValue))

def minList(x):
    min = x[0]
    for i in x:
        if i < min:
            min = i
    return min

minValue = minList(newList)
print("min value = " +str(minValue))

def searchPosition(x, z):
    position = x.index(z)
    return position

positionMaxValue = searchPosition(newList, maxValue)
print("Position max value = "+str(positionMaxValue))
positionMinValue = searchPosition(newList, minValue)
print("Position min value = "+str(positionMinValue))



