from random import *
import matplotlib.pyplot as plt
import csv
import numpy as np
import time


data = np.genfromtxt("/Users/computer/Desktop/ResearchTNOs/Data/tnoUnder_1.txt", delimiter = ",",names=True,dtype=None)
num = 83
for o in range(100):
	t0 = time.time()

	num += 1
	rndEccentricities = []
	rndInclinations = []

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
				if tdv < 1.01:
					tdv_Values.append(tdv)


	bins = np.arange(0.00, 1, 0.01)
	plt.hist(tdv_Values, bins, histtype="bar", rwidth = .075)
	print("saving...")
	plt.savefig('run'+str(num)+'.png')
	t1 = time.time()
	print(t1-t0)
