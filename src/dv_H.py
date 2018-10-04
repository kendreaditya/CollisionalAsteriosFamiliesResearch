# dv = abs(2.5*(a-b)/(a+b)) + abs(4*(f-e)/(f+e)) + abs(4*(k-j)/(k+j))

import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt("data/rawTNO.txt", delimiter = ";",names=True,dtype=None)
d_list = []
smallestdV = []
centerCollision = "2014LO28"
names = zip(*data)[0]
x = names.index(centerCollision)
zip(data)

for i in range(len(data)):
    dv = abs(2.5 * (data[x][2] - data[i][2]) / (data[x][2] + data[i][2])) + abs(4 * (data[i][3] - data[x][3]) / (data[i][3] + data[x][3])) + abs(4 * (data[i][4] - data[x][4]) / (data[i][4] + data[x][4]))
    dH = data[x][1] - data[i][1]
    d_list.append([dv, dH])


smallestdV = sorted(d_list, key=lambda dV: dV[0])[:50]
smallestdV = zip(*smallestdV)
plt.title("dv vs H")
plt.scatter(smallestdV[0], smallestdV[1])
plt.show()


