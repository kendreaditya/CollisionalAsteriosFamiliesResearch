import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import csv

colors = ['b.', 'g.', 'r.','c.','m.','y.','k.', '#eeffff', '#8a2be2', '#ffffff', '#030303', '#cd853f', '#ee3a8c']
clusters = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
data = pd.read_csv('/Users/computer/PycharmProjects/TNOsResearch/data/tnoList.csv')
x = data['a']
y = data['i']

plt.scatter(x, y, s = 1)

X = np.array(list(zip(x, y)))

kmenas = KMeans(n_clusters= len(colors))
kmenas.fit(X)

centroids = kmenas.cluster_centers_
labels = kmenas.labels_

print(centroids)
print(labels)


for i in range(len(x)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 1)
    dist = np.abs(centroids[labels[i]][0]-X[i][0])/(centroids[labels[i]][1]-X[i][1])
    clusters[labels[i]].append([data['name'][i], dist])

print(clusters)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=10, linewidths=5, zorder=10)


with open("tnoClustersAI.csv", "w+") as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=',')
    csvWriter.writerows(clusters)
plt.show()