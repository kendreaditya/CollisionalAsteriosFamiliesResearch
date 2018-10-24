import numpy as np
import matplotlib.pyplot as plt
import csv

data = np.genfromtxt("/Users/computer/Desktop/ResearchTNOs/Data/tdv_inclinationDEG.txt", delimiter = ",",names=True,dtype=None)
rangeBin = [5, 10, 15, 20, 25, 30, 35]
binedData = [[],[],[],[],[],[],[]]

for x in range(0, len(data)):
    incl = data[x][3], data[x][4], data[x][5]
    medianIncl = np.median(incl)
    for z in range(0, len(rangeBin)):
        if medianIncl <= rangeBin[z]:
            if data[x][6] <= .5:
                binedData[z].append(data[x][6])
            break
print(binedData[4])

plt.figure(1)
d = np.histogram(binedData[0], bins=np.arange(0, .51, 0.001))
d0 = list(d[0])
d1 = list(d[1])
del d1[-1]
plt.semilogy(d1, d0)

plt.figure(2)
d = np.histogram(binedData[1], bins=np.arange(0, .51, 0.01))
d0 = list(d[0])
d1 = list(d[1])
del d1[-1]
plt.semilogy(d1, d0)

plt.figure(3)
d = np.histogram(binedData[2], bins=np.arange(0, .51, 0.01))
d0 = list(d[0])
d1 = list(d[1])
del d1[-1]
plt.semilogy(d1, d0)

plt.figure(4)
d = np.histogram(binedData[3], bins=np.arange(0, .51, 0.01))
d0 = list(d[0])
d1 = list(d[1])
del d1[-1]
plt.semilogy(d1, d0)

plt.figure(5)
d = np.histogram(binedData[4], bins=np.arange(0, .51, 0.01))
d0 = list(d[0])
d1 = list(d[1])
del d1[-1]
plt.semilogy(d1, d0)

plt.figure(6)
d = np.histogram(binedData[5], bins=np.arange(0, .51, 0.01))
d0 = list(d[0])
d1 = list(d[1])
del d1[-1]
plt.semilogy(d1, d0)

plt.figure(7)
d = np.histogram(binedData[6], bins=np.arange(0, .51, 0.01))
d0 = list(d[0])
d1 = list(d[1])
del d1[-1]
plt.semilogy(d1, d0)
###################################################

plt.show()
