#tdv = 2.5*(max(a,b,c)-min(a,b,c))/median(a,b,c) + 4.0*(max(e,f,g)-min(e,f,g)) + 4.0*(max(j,k,l)-min(j,k,l))

import csv
import numpy as np

data = np.genfromtxt("/Users/computer/Desktop/ResearchTNOs/Data/tno.txt", delimiter = ",",names=True,dtype=None)

print(len(data))
fdv_Values = []

for x in range(len(data)/2, int(len(data)/(.75))):
    for i in range((len(data)/2)+1, int(len(data)/.75)):
        for y in range((len(data)/2)+1, int(len(data)/.75)):
            abc = [data[x][2], data[i-1][2], data[y-1][2]]
            efg = [data[x][3], data[i-1][3], data[y-1][3]]
            hij = [data[x][4], data[i-1][4], data[y-1][4]]
            fdv = 2.5*(max(abc)-min(abc))/np.median(abc) + 4.0*(max(efg)-min(efg)) + 4.0*(max(hij)-min(hij))
            fdv_Values.append([data[x][0], data[i-1][0], data[y-1][0], fdv])

fdv_Values.sort(key=lambda l:l[3])

with open("tdv_Values3.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(fdv_Values)

print(fdv_Values[0:100])
