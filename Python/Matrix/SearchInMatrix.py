from __future__ import print_function
import random
# find all paired values in the matrix and change by zero
matrix = []


def createMatrix():
    for i in range(4):
        matrix.append([random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)])
        # print (matrix)


def changeMatrix(matrix):
    for index1, el in enumerate(matrix):
        for index2, element in enumerate(el):
            if element % 2 == 0:
                matrix[index1][index2] = 0
                # print(matrix)


def tableMarix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()


createMatrix()
tableMarix(matrix)
changeMatrix(matrix)
print('\n')
tableMarix(matrix)