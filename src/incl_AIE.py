import numpy as np
import matplotlib.pyplot as plt
import csv

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
