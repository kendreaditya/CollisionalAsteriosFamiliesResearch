import matplotlib.pyplot
import numpy as np
import csv
# a = 3 (2)
# e = 2 (3)
data = np.genfromtxt("/Users/computer/Desktop/ResearchTNOs/Data/tnosALL.txt", delimiter = ",",names=True,dtype=None)

tiss_Values = []
an = 30.110387

for x in range(1, len(data)):
	tiss = (an/data[x][3]) + (2*data[x][4]) * (np.sqrt((an/data[x][3]) * (1-(data[x][2]**2))))
	tiss_Values.append(tiss)

n = []
g = []
s = []

for x in range(1, len(data)):
	n.append(data[x][1])
	'''
	g.append(data[x][6])
	s.append(data[x][7])
	'''

'''
matplotlib.pyplot.figure(1)
matplotlib.pyplot.title("tiss vs n")
matplotlib.pyplot.scatter(tiss_Values,n, .5)

matplotlib.pyplot.figure(2)
matplotlib.pyplot.title("tiss vs g")
matplotlib.pyplot.scatter(tiss_Values,g, .5)

matplotlib.pyplot.figure(3)
matplotlib.pyplot.title("tiss vs s")
matplotlib.pyplot.scatter(tiss_Values,s, .5)
#------------------------------------
'''
matplotlib.pyplot.figure(4)
matplotlib.pyplot.title("n vs tiss")
matplotlib.pyplot.scatter(n,tiss_Values, .5)
'''
matplotlib.pyplot.figure(5)
matplotlib.pyplot.title("g vs tiss")
matplotlib.pyplot.scatter(g,tiss_Values, .5)

matplotlib.pyplot.figure(6)
matplotlib.pyplot.title("s vs tiss")
matplotlib.pyplot.scatter(s,tiss_Values, .5)
'''
matplotlib.pyplot.show()
'''

with open("tiss_Values.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(tiss_Values)
'''
