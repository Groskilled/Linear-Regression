#!/usr/bin/python

import csv
import sys
import matplotlib.pyplot as plt
import numpy as np

def gradientDescent(X, Y, theta0, theta1):
    alpha = 0.0001
    while (1):
        hyp = (theta0 + X * theta1) - Y
        tmptheta0 = (alpha / X.ndim) * hyp.sum()
        tmptheta1 = (alpha / X.ndim) * (hyp * X).sum()
        if (abs(tmptheta0) < 0.000001 and abs(tmptheta1) < 0.000001):
            return[theta0 * 10000, theta1]
        else:
            theta0 = theta0 - tmptheta0
            theta1 = theta1 - tmptheta1

def main():
    cr = csv.reader(open("../../Data.csv","rb"))
    X = []
    Y = []
    for row in cr:
        X.append(float(row[0]) / 10000)
        Y.append(float(row[1]) / 10000)
    X = np.array(X, dtype=float)
    Y = np.array(Y, dtype=float)
    theta = gradientDescent(X, Y, 0.0, 0.0)
    X = X * 10000
    Y = Y * 10000
    Yest = theta[0] + X * theta[1]
    plt.plot(X, Y, 'ro')
    plt.plot(X, abs(Yest))
    plt.show()
    while (1):
        print("Unter a mileage.")
        ret = int(sys.stdin.readline())
        print("Estimated mileage is : %d" %(theta[0] + theta[1] * ret))

if __name__ == "__main__":
    main()
