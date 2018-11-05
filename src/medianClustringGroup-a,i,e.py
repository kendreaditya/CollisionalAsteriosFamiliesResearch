# dv = abs(2.5*(a-b)/(a+b)) + abs(4*(f-e)/(f+e)) + abs(4*(k-j)/(k+j))
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.genfromtxt("data/rawTNO.txt", delimiter = ";",names=True,dtype=None)
fig = plt.figure()
ax = Axes3D(fig)

obj = []
dv_Values = []
potentDV = []

for x in range(len(data)):
    for i in range(len(data)):
        dv = abs(2.5*(data[x][2]-data[i][2])/(data[x][2]+data[i][2]))+abs(4*(data[i][3]-data[x][3])/(data[i][3]+data[x][3]))+abs(4*(data[i][4]-data[x][4])/(data[i][4]+data[x][4]))
        dv_Values.append([dv, data[i][2], data[i][3], data[i][4]])

    dv_Values.sort()
    ax.scatter(dv_Values[5][1], dv_Values[5][2], dv_Values[5][2], s=4, c="blue")
    dv_Values.remove(dv_Values[5])
    dv_Values.remove(dv_Values[0])
    dv_Values = zip(*dv_Values)
    ax.scatter(dv_Values[1], dv_Values[2], dv_Values[3], s=2, c="red")
    dv_Values = []
    
plt.savefig("graphs/Clustering/medianClusteringMaster.png")
plt.show()
