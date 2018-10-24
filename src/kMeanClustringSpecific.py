import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import pandas as pd
import math as mt
import csv


#plt.rcParams['figure.figsize'] = (16, 9)

#colors = ['b.', 'g.', 'r.','c.','m.','y.','k.', '#eeffff', '#8a2be2', '#ffffff', '#030303', '#cd853f', '#ee3a8c']
colors = ['b.', 'w.', 'w.','w.','w.','w.','w.', 'w.', 'w.', '.', 'w.', 'w.', 'w.']

clusters = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
data = pd.read_csv('/Users/adityakendre/PycharmProjects/CollisionalAsteriosFamiliesResearch/src/data/tnoList.csv')
x = data['a']
y = data['i']
z = data['e']

fig = plt.figure()
ax = Axes3D(fig)
#ax = plt

X = np.array(list(zip(x, y, z)))

# Initializing KMeans
kmeans = KMeans(n_clusters= 13)
# Fitting with inputs
kmeans = kmeans.fit(X)
# Predicting the clusters
labels = kmeans.predict(X)
# Getting the cluster centers
print(labels)
centroids = kmeans.cluster_centers_

a = data['name']
itr = [index for index in range(len(a)) if a[index] == '148112']

for i in range(len(y)):
    if labels[i] == labels[itr]:
        ax.scatter(x[i], y[i], z[i], c = "red", s = 1)
    else:
        ax.scatter(x[i], y[i], z[i], c ="white", s=1)
    dist = np.abs((centroids[labels[i]][0] - X[i][0]) + (centroids[labels[i]][1] - X[i][1]) + (centroids[labels[i]][2] - X[i][2]))
    clusters[labels[i]].append([data['name'][i], mt.sqrt(dist)], )

ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2], marker='x', s=10, linewidths=5, zorder=10, c = 'black')
#clusters = zip(clusters)

with open("3DtnoClusters.csv", "w+") as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=',')
    csvWriter.writerow(clusters)

plt.show()
