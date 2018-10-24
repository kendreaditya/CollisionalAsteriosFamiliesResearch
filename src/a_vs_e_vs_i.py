import matplotlib.pyplot
import numpy as np

data = np.genfromtxt("/Users/computer/Desktop/ResearchTNOs/Data/tno.txt", delimiter = ",",names=True,dtype=None)

a = []
e = []
i = []

for x in range(1, len(data)):
	a.append(data[x][2])
	e.append(data[x][3])
	i.append(data[x][4])

matplotlib.pyplot.figure(1)
matplotlib.pyplot.title("a vs e")
matplotlib.pyplot.scatter(a,e, .5)

matplotlib.pyplot.figure(2)
matplotlib.pyplot.title("a vs i")
matplotlib.pyplot.scatter(a,i, .5)

matplotlib.pyplot.figure(3)
matplotlib.pyplot.title("e vs i")
matplotlib.pyplot.scatter(e,i, .5)

matplotlib.pyplot.show()
