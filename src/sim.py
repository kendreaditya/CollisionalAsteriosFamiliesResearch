from random import *
import matplotlib.pyplot as plt
import csv
import numpy as np

data = np.genfromtxt("/Users/computer/Desktop/ResearchTNOs/Data/tno.txt", delimiter = ",",names=True,dtype=None)

for y in range(100):

	rndEccentricities = []
	rndInclinations = []

	newData = list(zip(*data))
	newData[3] = list(newData[3])
	newData[3] = sorted(newData[3], key=lambda k: random())

	newData[4] = list(newData[4])
	newData[4] = sorted(newData[4], key=lambda k: random())


	data = list(zip(*newData))

	dv_Values = []

	for x in range(1, 1185):
		for i in range(x+1, 1185):
			dv = abs(2.5*(data[x][2]-data[i][2])/(data[x][2]+data[x][2])) + abs(4*(data[i][3]-data[x][3])/(data[i][3]+data[x][3])) + abs(4*(data[i][4]-data[x][4])/(data[i][4]+data[x][4]))
			dv_Values.append(dv)

	dv_Values.sort()


	bins = np.arange(0.00, 1, 0.01)
	plt.hist(dv_Values, bins, histtype="bar", rwidth = .075)
	plt.savefig('run'+str(y)+'.png')
