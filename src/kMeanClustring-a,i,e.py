import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import pandas as pd
import math as mt
import csv


amountClusters = 50

clusters = [[] for i in range(amountClusters)]

data = pd.read_csv('/Users/adityakendre/PycharmProjects/CollisionalAsteriosFamiliesResearch/src/data/tnoList.csv')
x = data['a']
y = data['i']
z = data['e']
a = data['name']

X = np.array(list(zip(x, y, z)))
fig = plt.figure()
ax = Axes3D(fig)

kmeans = KMeans(n_clusters=amountClusters)
kmeans = kmeans.fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_

for i in range(len(y)):
    dist = np.abs((centroids[labels[i]][0] - X[i][0])**2 + (centroids[labels[i]][1] - X[i][1])**2 + (centroids[labels[i]][2] - X[i][2])**2)
    clusters[labels[i]].append([data['name'][i], mt.sqrt(dist)])


with open('/Users/adityakendre/PycharmProjects/CollisionalAsteriosFamiliesResearch/src/data/KMeansClustring'+str(amountClusters)+'.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows(clusters)

itr = [index for index in range(len(a)) if a[index] == '120178']

for i in range(len(y)):
    if labels[i] == labels[itr]:
        ax.scatter(x[i], y[i], z[i], c="red", s=1)
    else:
        ax.scatter(x[i], y[i], z[i], c="blue", s=1)

ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2], marker='x', s=10, linewidths=5, zorder=10, c = 'black')
plt.show()
