# dv = abs(2.5*(a-b)/(a+b)) + abs(4*(f-e)/(f+e)) + abs(4*(k-j)/(k+j))

import numpy as np
import matplotlib.pyplot as plt
import random as rnd

data = np.genfromtxt("data/rawTNO.txt", delimiter=";", names=True, dtype=None)

for x in range(len(data)):
    d_list = []
    smallestdV = []
    #x = rnd.randint(0, len(data))
    for i in range(len(data)):
        dv = abs(2.5 * (data[x][2] - data[i][2]) / (data[x][2] + data[i][2])) + abs(4 * (data[i][3] - data[x][3]) / (data[i][3] + data[x][3])) + abs(4 * (data[i][4] - data[x][4]) / (data[i][4] + data[x][4]))
        dH = data[x][1] - data[i][1]
        d_list.append([dv, dH])


    smallestdV = sorted(d_list, key=lambda dV: dV[0])[:50]
    smallestdV = zip(*smallestdV)
    plt.title("dv vs H")
    plt.gca().set_xlim([0, 1.5])
    plt.gca().set_ylim([0, 5])
    plt.scatter(smallestdV[0], smallestdV[1])
    plt.savefig("graphs/Collison Center/" + data[x][0]+".png")
    plt.gcf().clear()


