#tdv = 2.5*(max(a,b,c)-min(a,b,c))/median(a,b,c) + 4.0*(max(e,f,g)-min(e,f,g)) + 4.0*(max(j,k,l)-min(j,k,l))

import csv
import numpy as np

data = np.genfromtxt("/Users/computer/Desktop/ResearchTNOs/Data/tno.txt", delimiter = ",",names=True,dtype=None)

print(len(data))
fdv_Values = []

for x in range(int(len(data)/.75), len(data)):
    for i in range(int((len(data)/.75))+1, len(data)):
        for y in range(int((len(data)/.75))+1, len(data)):
            abc = [data[x][2], data[i][2], data[y][2]]
            efg = [data[x][3], data[i][3], data[y][3]]
            hij = [data[x][4], data[i][4], data[y][4]]
            fdv = 2.5*(max(abc)-min(abc))/np.median(abc) + 4.0*(max(efg)-min(efg)) + 4.0*(max(hij)-min(hij))
            fdv_Values.append([data[x][0], data[i][0], data[y][0], fdv])

fdv_Values.sort(key=lambda l:l[3])

with open("tdv_Values4.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(fdv_Values)

print(fdv_Values[0:100])
