# Created by Vinay Jakkali on 11/25/2019

"""
--------------------------------------------------------------------------------------
Problem 4. function takes the following inputs

INPUT:

X0 - It takes a float value, which acts as an initial guess to Newton-Raphson Method
m - It takes a float value and it represents the slope of the input line
n - It is the no. of points that are being mapped. It takes an integer value >0
D_range - It is the range defined for the graph
b - is the y-intercept and takes a float values
eps - represents the magnitude of the noise in the input data

OUTPUT:
Plots showing objective function with the minimum point and the best fit line along with original data
Also prints the values of minimum x, minimum F(x) to the console

--------------------------------------------------------------------------------------
"""

import numpy as np
import random
import JakkaliVinay_Assignment1,

import matplotlib.pyplot as plt


def total_least_squares(x0=0.1, m=0.5, n=1000, d_range=(0, 5), b=0.0, eps=1e-2):
    """"""
    ri = random.random()  # ri represents Ri from equation y = mx+b+e(Ri-1)
    x = np.linspace(d_range[0], d_range[1], n)
    x = np.array(x)
    y = lambda x: x * m + b + eps * (2 * ri - 1)
    y = np.array(y(x))
    z = lambda a: (x + a * y) / (a ** 2 + 1)
    f_a = lambda a: sum((x - z(a)) ** 2 + (y - a * z(a)) ** 2)
    a, ok = NR(f_a, x0)
    print("The optimized value of a is = ", round(a, 4))
    print("The value of objective function F(a) = ", round(f_a(a), 4))
    plt.scatter(x, y, color='green', marker='o')
    plt.plot(x, a * x, color='red', Linewidth=2)
    plt.title("Least Squares Method", fontsize=24)
    plt.xlabel("x axis", fontsize=24)
    plt.ylabel("y axis", fontsize=24)
    plt.legend(("Best Fit Line", "Actual Data"), fontsize=20)
    plt.xlim(d_range[0], d_range[1])
    plt.ylim(d_range[0], d_range[1] - 2)
    plt.grid()
    # plt.axes().set_aspect('equal')
    plt.axes().axhline(y=0, color='k')
    plt.axes().axvline(x=0, color='k')
    plt.show()


total_least_squares()



