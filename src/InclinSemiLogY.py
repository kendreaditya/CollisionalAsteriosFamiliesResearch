import numpy as np
import matplotlib.pyplot as plt
import csv
import time
from random import *
import math

dataReal = np.genfromtxt("/Users/computer/Desktop/ResearchTNOs/ResearchTNOs/Data/tdv_inclinationDEG.txt", delimiter = ",",names=True,dtype=None)
data1 = np.genfromtxt("tdv_ValuesRND1.txt", delimiter = ",",names=True,dtype=None)
data2 = np.genfromtxt("tdv_ValuesRND2.txt", delimiter = ",",names=True,dtype=None)
data3 = np.genfromtxt("tdv_ValuesRND3.txt", delimiter = ",",names=True,dtype=None)
data4 = np.genfromtxt("tdv_ValuesRND4.txt", delimiter = ",",names=True,dtype=None)
data5 = np.genfromtxt("tdv_ValuesRND5.txt", delimiter = ",",names=True,dtype=None)
data6 = np.genfromtxt("tdv_ValuesRND6.txt", delimiter = ",",names=True,dtype=None)
data7 = np.genfromtxt("tdv_ValuesRND7.txt", delimiter = ",",names=True,dtype=None)
data8 = np.genfromtxt("tdv_ValuesRND8.txt", delimiter = ",",names=True,dtype=None)
data9 = np.genfromtxt("tdv_ValuesRND9.txt", delimiter = ",",names=True,dtype=None)
data0 = np.genfromtxt("tdv_ValuesRND0.txt", delimiter = ",",names=True,dtype=None)
data = [dataReal, data0, data1, data2, data3, data4, data5, data6, data7, data8, data9]




for j in range(10):
    print(len(data[j]))
    rangeBin = [5, 10, 15, 20, 25, 30, 35]
    binedData = [[], [], [], [], [], [], []]
    for x in range(0, len(data[j])):
        incl = data[j][x][3], data[j][x][4], data[j][x][5]
        medianIncl = np.median(incl)
        for z in range(0, len(rangeBin)):
            if medianIncl <= rangeBin[z]:
                if data[j][x][6] <= .5:
                    binedData[z].append(data[j][x][6])
                break
    plt.figure(1)
    d = np.histogram(binedData[0], bins=np.arange(0, .51, 0.01))
    d0 = list(d[0])
    d1 = list(d[1])
    del d1[-1]
    plt.semilogy(d1, d0)
    #
    plt.figure(2)
    d = np.histogram(binedData[1], bins=np.arange(0, .51, 0.01))
    d0 = list(d[0])
    d1 = list(d[1])
    del d1[-1]
    plt.semilogy(d1, d0)
    #
    plt.figure(3)
    d = np.histogram(binedData[2], bins=np.arange(0, .51, 0.01))
    d0 = list(d[0])
    d1 = list(d[1])
    del d1[-1]
    plt.semilogy(d1, d0)
    #
    plt.figure(4)
    d = np.histogram(binedData[3], bins=np.arange(0, .51, 0.01))
    d0 = list(d[0])
    d1 = list(d[1])
    del d1[-1]
    plt.semilogy(d1, d0)
    #
    plt.figure(5)
    d = np.histogram(binedData[4], bins=np.arange(0, .51, 0.01))
    d0 = list(d[0])
    d1 = list(d[1])
    del d1[-1]
    plt.semilogy(d1, d0)
    #
    plt.figure(6)
    d = np.histogram(binedData[5], bins=np.arange(0, .51, 0.01))
    d0 = list(d[0])
    d1 = list(d[1])
    del d1[-1]
    plt.semilogy(d1, d0)
    #
    plt.figure(7)
    d = np.histogram(binedData[6], bins=np.arange(0, .51, 0.01))
    d0 = list(d[0])
    d1 = list(d[1])
    del d1[-1]
    plt.semilogy(d1, d0)

###################################################

plt.show()