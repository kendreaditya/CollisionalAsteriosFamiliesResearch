#dv = abs(2.5*(a-b)/(a+b)) + abs(4*(f-e)/(f+e)) + abs(4*(k-j)/(k+j))

import csv
import numpy as np

data = np.genfromtxt("/Users/computer/Desktop/ResearchTNOs/Data/tno.txt", delimiter = ",",names=True,dtype=None)

dv_Values = []
potentDV = []

for x in range(1, 1185):
	for i in range(x+1, 1185):
		dv = abs(2.5*(data[x][2]-data[i][2])/(data[x][2]+data[x][2])) + abs(4*(data[i][3]-data[x][3])/(data[i][3]+data[x][3])) + abs(4*(data[i][4]-data[x][4])/(data[i][4]+data[x][4]))
		dv_Values.append([data[x][0], data[i][0], dv])

		if dv < .1:
			potentDV.append(list(data[x]))
			potentDV.append(list(data[i]))

dv_Values.sort(key=lambda l:l[2])
'''
with open("dv_Values.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(dv_Values)
'''

potentFam = []
for c in potentDV:
	if c not in potentFam:
		potentFam.append(c)

potentDV = list(potentDV)
with open("/Users/computer/Desktop/ResearchTNOs/Data/tno_rc.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(potentFam)
