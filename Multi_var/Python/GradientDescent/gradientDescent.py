#!/usr/bin/python

from __future__ import division
from math import sqrt
import csv
import sys
import matplotlib.pyplot as plt
import numpy as np

def gradientDescent(size, room, Y):
    alpha = 0.1
    theta0 = 0.0
    theta1 = 0.0
    theta2 = 0.0
    while(1):
        hyp = (theta0 + size * theta1 + room * theta2) - Y
        tmptheta0 = (alpha / len(size)) * hyp.sum()
        tmptheta1 = (alpha / len(size)) * (hyp * size).sum()
        tmptheta2 = (alpha / len(size)) * (hyp * room).sum()
        if (abs(tmptheta0) < 0.001 and abs(tmptheta1) < 0.001 and abs(tmptheta2) < 0.001):
            return ([theta0, theta1, theta2])
        else:
            theta0 = theta0 - tmptheta0
            theta1 = theta1 - tmptheta1
            theta2 = theta2 - tmptheta2

def main():
    cr = csv.reader(open("../../Data.csv","rb"))
    size = [] 
    room = [] 
    Y = []
    for row in cr:
        size.append(float(row[0]))
        room.append(float(row[1]))
        Y.append(float(row[2]))
    size = np.array(size)
    room = np.array(room)
    size = (size - np.mean(size)) / (np.ptp(size))
    room = (room - np.mean(room)) / (np.ptp(room))
    theta = gradientDescent(size, room, Y)
    while (1):
        print("Unter a size.")
        a1 = float(sys.stdin.readline())
        print("Unter a number or bedrooms.")
        a2 = float(sys.stdin.readline())
        print("Estimated price is : %d" %(theta[0] + (theta[1] * (a1 - 2000.0) / 3626.0) + (theta[2] * (a2 - 3.0) / 4.0)))

if __name__ == "__main__":
    main()
