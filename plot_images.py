import matplotlib.pyplot as plt
import matplotlib.patches as pth
import numpy as np

def plotRectangles(iterations):
    fig, ax = plt.subplots()

    for elem in iterations:
        x1_low = min(elem[0][0])
        x1_high = max(elem[0][0])
        x2_low = min(elem[1][0])
        x2_high = max(elem[1][0])
        ax.add_patch(
            pth.Rectangle((x1_low, x2_low), (x1_high - x1_low), (x2_high - x2_low),
                            linewidth=1, edgecolor='r', facecolor='none'))

    ax.plot()
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.show()

def plotRadius(iterations, start_iter):
    radius = []
    num_iter = []

    for i in range(len(iterations)):
        x1_len = (max(iterations[i][0][0]) - min(iterations[i][0][0])) / 2
        x2_len = (max(iterations[i][1][0]) - min(iterations[i][1][0])) / 2
        radius.append(x1_len ** 2 + x2_len ** 2)
        num_iter.append(i + start_iter)

    plt.plot(num_iter, radius)
    plt.xlabel("Номер итерации")
    plt.ylabel("Длина радиуса")
    plt.show()
