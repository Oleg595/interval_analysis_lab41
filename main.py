import math
from copy import deepcopy
from plot_images import plotRectangles, plotRadius

def sum(i1, i2):
    return [i1[0] + i2[0], i1[1] + i2[1]]

def sub(i1, i2):
    return [i1[0] - i2[0], i1[1] - i2[1]]

def mul(i1, i2):
    return [i1[0] * i2[0], i1[1] * i2[1]]

def div(i1, i2):
    return [i1[0] / i2[1], i1[1] / i2[0]]

def diversion(i1):
    x = 0.
    y = 0.
    if i1[0] != 0:
        x = 1. / i1[0]
    if i1[1] != 0:
        y = 1. / i1[1]
    return [x, y]

def mulMatrix(A, B):
    result = []
    for i in range(len(A)):
        result.append([])
        for j in range(len(B[i])):
            result[i].append([0, 0])
            for q in range(len(A[i])):
                result[i][j] = sum(result[i][j], mul(A[i][q], B[q][j]))
    return result

def subMatrix(A, B):
    result = deepcopy(A)
    for i in range(len(result)):
        for j in range(len(result[i])):
            result[i][j] = sub(result[i][j], B[i][j])
    return result

def inversionMatrix(D):
    result = deepcopy(D)
    for i in range(len(result)):
        for j in range(len(result[i])):
            result[i][j] = diversion(result[i][j])
    return result

def equal(oldX, newX):
    e = 10 ** -10
    for i in range(len(oldX)):
        for j in range(len(oldX[i])):
            divX = sub(oldX[i][j], newX[i][j])
            if math.fabs(divX[0]) > e or math.fabs(divX[1]) > e:
                return False
    return True

D = [[[3, 4], [0, 0]], [[0, 0], [4, 5]]]
inversionD = inversionMatrix(D)
E = [[[0, 0], [0, 1]], [[-1, 2], [0, 0]]]
d = [[[3, 5]], [[0, 1]]]
oldX = [[[-1, 1]], [[-1, 1]]]

Ex = mulMatrix(E, oldX) #Ex(0)
dEx = subMatrix(d, Ex) #d-Ex(0)
newX = mulMatrix(inversionD, dEx) #(invD)(d-Ex(0))

iterations = [oldX, newX]

while not equal(oldX, newX):
    oldX = deepcopy(newX)

    Ex = mulMatrix(E, oldX)
    dEx = subMatrix(d, Ex)
    newX = mulMatrix(inversionD, dEx)

    iterations.append(newX)

plotRectangles(iterations[:int(len(iterations) / 2)])
plotRadius(iterations[:int(len(iterations) / 2)], 0)

plotRectangles(iterations[int(len(iterations) / 2):len(iterations)])
plotRadius(iterations[int(len(iterations) / 2):len(iterations)], int(len(iterations) / 2))
