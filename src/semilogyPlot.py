from random import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import csv
import numpy as np
import time
data = np.genfromtxt("/Users/computer/Desktop/ResearchTNOs/Data/tnoUnder_1.txt", delimiter = ",",names=True,dtype=None)

for i in range(5):
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
					tdv_Values.append(tdv)
	tdv_Values.sort()
	print(len(tdv_Values))
	col = ["blue", "green", "cyan", "magenta", "yellow", "red", "#a3a5cc", "#c45ac4", "#c4ad5a", "#b2cca3"]
	d = np.histogram(tdv_Values, bins=np.arange(0, .5, .01))
	d0 = list(d[0])
	d1 = list(d[1])
	del d1[-1]
	plt.semilogy(d1, d0)
	t1 = time.time()
	print(t1-t0)
	RNDpatch = mpatches.Patch(label='random run #' + str(i+1))
	plt.legend(handles=[RNDpatch])
	print("done!")

t10 = time.time()
data = np.genfromtxt("/Users/computer/Desktop/ResearchTNOs/Data/tnoUnder_1.txt", delimiter = ",",names=True,dtype=None)
tdvValues = []
freq = []


for x in range(1, len(data)):
	for i in range(x+1, len(data)):
		for y in range(i+1, len(data)):

			abc = [data[x][2], data[i][2], data[y][2]]
			efg = [data[x][3], data[i][3], data[y][3]]
			hij = [data[x][4], data[i][4], data[y][4]]
			tdv = 2.5*(max(abc)-min(abc))/np.median(abc) + 4.0*(max(efg)-min(efg)) + 4.0*(max(hij)-min(hij))

			if tdv <= .5:
				tdvValues.append(tdv)
tdvValues.sort()


u = np.histogram(tdvValues, bins=np.arange(0, .5, .01))
u0 = list(u[0])
u1 = list(u[1])
del u1[-1]
patch = mpatches.Patch(color="black", label="Real Data")
plt.legend(handles=[patch])
plt.semilogy(u1, u0)
t2 = time.time()
print(t2-t10)
plt.show()
