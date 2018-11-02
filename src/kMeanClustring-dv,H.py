import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import pandas as pd
import math as mt
import csv

amountClusters = 13
clusters = [[] for i in range(amountClusters)]

data = np.genfromtxt("data/rawTNO.txt", delimiter = ";",names=True,dtype=None)
d_list = []
smallestdV = []
centerCollision = "2014LO28"
names = zip(*data)[0]
x = names.index(centerCollision)
zip(data)

for i in range(len(data)):
    dv = abs(2.5 * (data[x][2] - data[i][2]) / (data[x][2] + data[i][2])) + abs(4 * (data[i][3] - data[x][3]) / (data[i][3] + data[x][3])) + abs(4 * (data[i][4] - data[x][4]) / (data[i][4] + data[x][4]))
    dH = data[x][1] - data[i][1]
    d_list.append([dv, dH])

X = np.array(d_list)

kmeans = KMeans(n_clusters=amountClusters)
kmeans = kmeans.fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_

for i in range(len(d_list)):
    dist = np.abs((centroids[labels[i]][0] - X[i][0])**2 + (centroids[labels[i]][1] - X[i][1])**2)
    clusters[labels[i]].append([names[i], mt.sqrt(dist)])
    #clusters[labels[i]].append([data['name'][i]])


with open('/Users/adityakendre/PycharmProjects/CollisionalAsteriosFamiliesResearch/src/data/KMeansClustring(dv,H)'+str(amountClusters)+'.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows(clusters)

itr = [index for index in range(len(names)) if names[index] == '19308']

for i in range(len(d_list)):
    if labels[i] == labels[itr]:
        plt.scatter(d_list[i][0], d_list[i][1], 1,color="red")
    else:
        plt.scatter(d_list[i][0], d_list[i][1], 1, color="blue")

plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', linewidths=5, zorder=10, c = 'black')

plt.show()