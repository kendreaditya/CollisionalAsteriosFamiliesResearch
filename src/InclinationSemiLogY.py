import numpy as np
import matplotlib.pyplot as plt
import csv
import time
from random import *
import math

data = np.genfromtxt("/Users/computer/Desktop/ResearchTNOs/Data/tnoUnder_1.txt", delimiter = ",",names=True,dtype=None)

for i in range(10):
	t0 = time.time()
	freq = []

	newData = list(zip(*data))
	newData[3] = list(newData[3])
	newData[3] = sorted(newData[3], key=lambda k: random())

	newData[4] = list(newData[4])
	newData[4] = sorted(newData[4], key=lambda k: random())

	data = list(zip(*newData))
	tdv_Values = []

	for x in range(1, len(data)):
		for i in range(x+1, len(data)):
			for y in range(i+1, len(data)):

				abc = [data[x][2], data[i][2], data[y][2]]
				efg = [data[x][3], data[i][3], data[y][3]]
				hij = [data[x][4], data[i][4], data[y][4]]
				tdv = 2.5*(max(abc)-min(abc))/np.median(abc) + 4.0*(max(efg)-min(efg)) + 4.0*(max(hij)-min(hij))
				if tdv <= .5:
					tdv_Values.append([tdv, data[x][4], data[i][4], data[y][4]])

	rangeBin = [5, 10, 15, 20, 25, 30, 35]
	binedData = [[],[],[],[],[],[],[]]

	for u in range(0, len(tdv_Values)):
		incl = [tdv_Values[u][1], tdv_Values[u][2], tdv_Values[u][3]]
		medianIncl = np.degrees(np.median(incl))
		print(medianIncl)
		for z in range(0, len(rangeBin)):
			if medianIncl <= rangeBin[z]:
				if tdv_Values[u][0] <= rangeBin[z]:
					binedData[z].append(tdv_Values[u][0])
           		break

	print(binedData)
	plt.figure(1)
	d = np.histogram(binedData[0], bins=np.arange(0, .51, 0.01))
	print(d)
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

	t1 = time.time()
	print(t1-t0)

###################################################
data = np.genfromtxt("/Users/computer/Desktop/ResearchTNOs/Data/tdv_inclinationDEG.txt", delimiter = ",",names=True,dtype=None)
rangeBin = [5, 10, 15, 20, 25, 30, 35]
binedData = [[],[],[],[],[],[],[]]

for x in range(1, len(data)):
    incl = data[x][3], data[x][4], data[x][5]
    medianIncl = np.median(incl)
    for z in range(0, len(rangeBin)):
        if medianIncl <= rangeBin[z]:
            if data[x][6] <= .5:
                binedData[z].append(data[x][6])
            break
print(binedData[0])

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

plt.show()
