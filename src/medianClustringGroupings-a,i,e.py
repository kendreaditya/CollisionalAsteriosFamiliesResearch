# dv = abs(2.5*(a-b)/(a+b)) + abs(4*(f-e)/(f+e)) + abs(4*(k-j)/(k+j))
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.backends.backend_pdf

data = np.genfromtxt("data/rawTNO.txt", delimiter = ";",names=True,dtype=None)
fig = plt.figure()
ax = Axes3D(fig)
pdf = matplotlib.backends.backend_pdf.PdfPages("graphs/Clustering/allMedianClusterings.pdf")


obj = []
dv_Values = []
potentDV = []

for x in range(len(data)):
    for i in range(len(data)):
        dv = abs(2.5*(data[x][2]-data[i][2])/(data[x][2]+data[i][2]))+abs(4*(data[i][3]-data[x][3])/(data[i][3]+data[x][3]))+abs(4*(data[i][4]-data[x][4])/(data[i][4]+data[x][4]))
        dv_Values.append([dv, data[i][2], data[i][3], data[i][4], data[i][0], data[x][0]])

    dv_Values.sort()

    dv_Values = dv_Values[:11]
    ax.scatter(dv_Values[5][1], dv_Values[5][2], dv_Values[5][2], s=4, c="blue")
    dv_Values.remove(dv_Values[5])
    dv_Values.remove(dv_Values[0])

    dv_Values = zip(*dv_Values)
    ax.scatter(dv_Values[1], dv_Values[2], dv_Values[3], s=2, c="red")

    plt.rcParams.update({'font.size': 6})
    ax.set_title("Center: " + dv_Values[5][1] + "\n including: " + str(dv_Values[4]))

    ax.set_xlabel('a')
    ax.set_ylabel('i')
    ax.set_zlabel('e')

    ax.set_xlim(25, 75)
    ax.set_ylim(0.0, 0.6)
    ax.set_zlim(0.0, 0.35)


    pdf.savefig()
    plt.cla()

    dv_Values = []

pdf.close()
