import random
# found in two lists of unique elements, and write them into the third


def createList(x):
    list = [random.randint(0, 20) for x in range(x)]
    return list


def searchValues(a, b):
    list3 = list(set(a) - set(b))
    print(list3)


# operations with set
def testSet(a, b):
    set1 = set(a)
    set2 = set(b)
    list3 = set1 | set2
    list4 = set1 & set2
    list5 = set1 - set2
    list6 = set1 ^ set2
    print("merger two list " + str(list3))
    print("crossing two list " + str(list4))
    print("difference two list " + str(list5))
    print("difference two list " + str(list6))


list1 = createList(20)
list2 = createList(20)

print(list1)
print(list2)
searchValues(list1, list2)
print("\n")
testSet(list1, list2)




