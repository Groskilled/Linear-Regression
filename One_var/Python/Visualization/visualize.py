#!/usr/bin/python

import csv
import matplotlib.pyplot as plt

cr = csv.reader(open("../Data.csv","rb"))
X = []
Y = []
for row in cr:
    X.append(int(row[0]))
    Y.append(int(row[1]))
print(X)
print(Y)
plt.plot(X, Y, 'ro')
plt.show()
