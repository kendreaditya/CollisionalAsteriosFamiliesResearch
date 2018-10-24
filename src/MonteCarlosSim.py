from random import *
import matplotlib.pyplot as plt
import csv
import numpy as np

data = np.genfromtxt("/Users/computer/Desktop/ResearchTNOs/Data/tnoUnder_1.txt", delimiter = ",",names=True,dtype=None)

for o in range(10):

	rndEccentricities = []
	rndInclinations = []


	for y in range(1, 5000):
		rndEccentricities.append(uniform(0, .1))
		rndInclinations.append(np.sin(np.deg2rad(uniform(0, 180))))

	'''


    newData = list(zip(*data))
	newData[3] = list(newData[3])
	newData[3] = sorted(newData[3], key=lambda k: random())

	newData[4] = list(newData[4])
	newData[4] = sorted(newData[4], key=lambda k: random())


	data = list(zip(*newData))
	'''
	tdv_Values = []

	for x in range(1, len(data)):
		for i in range(x+1, len(data)):
			for y in range(i+1, len(data)):

				abc = [data[x][2], data[i][2], data[y][2]]
				efg = [rndEccentricities[x], rndEccentricities[i], rndEccentricities[y]]
				hij = [rndInclinations[x], rndInclinations[i], rndInclinations[y]]

				tdv = 2.5*(max(abc)-min(abc))/np.median(abc) + 4.0*(max(efg)-min(efg)) + 4.0*(max(hij)-min(hij))
				tdv_Values.append(tdv)
	'''
	dv_Values = []
	for x in range(1, 1185):
		for i in range(x+1, 1185):
			dv = abs(2.5*(data[x][2]-data[i][2])/(data[x][2]+data[x][2])) + abs(4*(data[i][3]-data[x][3])/(data[i][3]+data[x][3])) + abs(4*(data[i][4]-data[x][4])/(data[i][4]+data[x][4]))
			dv_Values.append(dv)

	dv_Values.sort()
	'''
	'''
	with open("dv_Values_rnd.csv","w+") as my_csv:
    	csvWriter = csv.writer(my_csv,delimiter=',')
    	csvWriter.writerows(dv_Values)

	with open("tnoRND.txt","w+") as my_csv:
    	csvWriter = csv.writer(my_csv,delimiter=',')
    	csvWriter.writerows(data)
	'''
	tdv_Values.sort()
	print(tdv_Values[0:5])
	'''
	bins = np.arange(0.00, 1, 0.01)
	plt.hist(tdv_Values, bins, histtype="bar", rwidth = .075)
	plt.savefig('runRND'+str(o)+'.png')
	print("saving...")
	'''
