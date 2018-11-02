# dv = abs(2.5*(a-b)/(a+b)) + abs(4*(f-e)/(f+e)) + abs(4*(k-j)/(k+j))
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.genfromtxt("data/rawTNO.txt", delimiter = ",",names=True,dtype=None)
fig = plt.figure()
ax = Axes3D(fig)

dv_Values = []
potentDV = []

for x in range(len(data)):
    for i in range(x+1, len(data)):
        dv = abs(2.5*(data[x][2]-data[i][2])/(data[x][2]+data[i][2]))+abs(4*(data[i][3]-data[x][3])/(data[i][3]+data[x][3]))+abs(4*(data[i][4]-data[x][4])/(data[i][4]+data[x][4]))
        dv_Values.append([data[x][0], data[i][0], dv, data[i][2], data[i][3], data[i][4]])

    sorted(dv_Values, key=lambda x: x[2])
    dv_Values = dv_Values[:10]
    ax.scatter(dv_Values[5][3], dv_Values[5][4], dv_Values[5][5], c="blue", s=1)
    dv_Values = []
plt.show()