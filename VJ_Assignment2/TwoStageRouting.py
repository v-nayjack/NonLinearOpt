# Created by Vinay Jakkali on 12/11/2019

"""
--------------------------------------------------------------------------------------
Include code description here:

--------------------------------------------------------------------------------------
"""

import numpy as np
import matplotlib.pyplot as plt


def routing_two(x, P1, C0, r, rho):

    A1 = x[0] ** 2 + x[1] ** 2  # one of the points is origin

    B1 = 2 * ((-C0[0] * x[0]) + (-C0[1] * x[1]))

    C1 = C0[0] ** 2 + C0[1] ** 2 - r ** 2

    D1 = (B1 ** 2) - (4 * A1 * C1)

    v1 = 0

    if D1 > 0:
        s11 = (-B1 + D1 ** 0.5) / (2 * A1)

        s21 = (-B1 - D1 ** 0.5) / (2 * A1)

        if s11 >= s21:
            t1 = s21
            s21 = s11
            s11 = t1


        if (s11 < 1 and s21 < 1) or (s11 < 0 and s21 < 0):

            v1 = (min(s21, 1) - max(s11, 0)) * (A1 ** 0.5)

        else:

            v1 = 0


    F1 = (A1 ** 0.5) + (rho * v1 ** 3)

    """Second Stage Calculations"""

    A2 = (P1[0] - x[0]) ** 2 + (P1[1] - x[1]) ** 2

    B2 = 2 * ((x[0] - C0[0]) * (P1[0] - x[0]) + (x[1] - C0[1]) * (P1[1] - x[1]))

    C2 = (x[0] - C0[0]) ** 2 + (x[1] - C0[1]) ** 2 - r ** 2

    D2 = (B2 ** 2) - (4 * A2 * C2)

    v2 = 0

    if D2 > 0:
        s12 = (-B2 + D2 ** 0.5) / (2 * A2)

        s22 = (-B2 - D2 ** 0.5) / (2 * A2)

        if s12 >= s22:
            t2 = s22
            s22 = s12
            s12 = t2


        if (s12 < 1 and s22 < 1) or (s12 < 0 and s22 < 0):

            v2 = (min(s22, 1) - max(s12, 0)) * (A2 ** 0.5)

        else:

            v2 = 0


    F2 = (A2 ** 0.5) + (rho * v2 ** 3)

    F = F1 + F2

    return F

def routing_plot(center, r, p, Inter_point):

    plt.figure()
    circle = plt.Circle(center, r, color='b', fill=False)
    plt.gcf().gca().add_artist(circle)
    plt.scatter(center[0], center[1], color='r', marker='*')
    plt.scatter(0, 0, color='g', marker='x')
    plt.scatter(Inter_point[0], Inter_point[1], color='r', marker='x')
    plt.scatter(p[0], p[1], color='b', marker='o')
    plt.plot([0, Inter_point[0]], [0, Inter_point[1]], color='r')
    plt.plot([Inter_point[0], p[0]], [Inter_point[1], p[1]], color='k')
    plt.title('Optimal Robot Path', fontsize=20)
    plt.xlabel('x axis', fontsize=16)
    plt.ylabel('y axis', fontsize=16)
    plt.xlim(0, 5.5)
    plt.ylim(0, 5.5)
    plt.grid(True)
    plt.axes().axhline(y=0, color='k')
    plt.axes().axvline(x=0, color='k')
    plt.axes().set_aspect('equal')

    return plt.show()

