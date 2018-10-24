import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt("tdv_Values.txt", delimiter = ",",names=True,dtype=None)

dv_Values = []

'''
for x in range(1, len(data)):
	for i in range(x+1, len(data)):
		dv = abs(2.5*(data[x][2]-data[i][2])/(data[x][2]+data[x][2])) + abs(4*(data[i][3]-data[x][3])/(data[i][3]+data[x][3])) + abs(4*(data[i][4]-data[x][4])/(data[i][4]+data[x][4]))
		dv_Values.append(dv)
'''

for x in range(len(data)):
	dv_Values.append(data[x][3])

bins = np.arange(0.00, 1, 0.01)
dv_Values.sort()
plt.hist(dv_Values, bins, histtype="bar", rwidth = .025)
plt.savefig('tdv_histogram.png')
