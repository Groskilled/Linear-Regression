#!/usr/bin/python

import csv
import sys
import matplotlib.pyplot as plt
import numpy as np

def main():
    cr = csv.reader(open("../Data.csv","rb"))
    X = []
    Y = []
    for row in cr:
        X.append([row[0], row[1]])
        Y.append(row[2])
    X = np.array(X)
    Y = np.array(Y)

if __name__ == "__main__":
    main()
