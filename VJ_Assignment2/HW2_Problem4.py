# Created by Vinay Jakkali on 12/9/2019

"""
--------------------------------------------------------------------------------------
Include code description here:

--------------------------------------------------------------------------------------
"""
import numpy as np
from PowellMethod import powell_method
from Quasi_Newton import quasi_newton


def f1(x):

    F1 = (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

    return F1

def f2(x):

    F2 = -1. * ((x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2)

    return F2

def main1():

    L = np.array([-10.0, -10.0])
    U = np.array([10.0, 10.0])
    x = np.linspace(L[0], U[0], 11)
    y = np.linspace(L[1], U[1], 11)
    Minima = []
    Maxima = []

    for i in x:
        for j in y:
            Minimums, k1 = powell_method(f1, [i, j], L, U)
            Maximums, k2 = powell_method(f2, [i, j], L, U)
            print("Minimums", Minimums)
            print("Maximums", Maximums)
            Minima.append(Minimums)
            Maxima.append(Maximums)
    print("Minima", Minima)
    print("Maxima", Maxima)


def main2():

    L = np.array([-5.0, -5.0])
    U = np.array([5.0, 5.0])
    x = np.linspace(L[0], U[0], 11)
    y = np.linspace(L[1], U[1], 11)
    Minima = []
    Maxima = []

    for i in x:
        for j in y:
            Minimums, k1 = quasi_newton(f1, [i, j])
            Maximums, k2 = quasi_newton(f2, [i, j])
            print("Minimums", Minimums)
            print("Maximums", Maximums)
            Minima.append(Minimums)
            Maxima.append(Maximums)
    print("Minima", Minima)
    print("Maxima", Maxima)









if __name__ == '__main__':
    main1()



