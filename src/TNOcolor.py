import numpy as np

data = np.genfromtxt("/Users/computer/Desktop/ResearchTNOs/Data/tnocol.txt", delimiter = ",",names=True,dtype=None)
tno = np.genfromtxt("/Users/computer/Desktop/ResearchTNOs/Data/tno.txt", delimiter = ",",names=True,dtype=None)

data = list(data)
tno = list(tno)

tnoList = []

for x in range(len(data)):
    data[x][1] = str(data[x][0]) + str(data[x][1])

for i in range(len(tno)):
    for y in range(len(data)):
        print(tno[i][0])
        print(data[y][1])
        if tno[i][0] == data[y][1]:
            append.tnoList(data[y])
print(tnoList)
