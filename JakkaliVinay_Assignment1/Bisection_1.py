# Created by Vinay Jakkali on 11/25/2019

"""
_________________________________________________________________
Include code description here:

_________________________________________________________________
"""


import numpy as np
import matplotlib.pyplot as plt


def bisection(f, a, b, tol=1e-8, maxiter=1e3):

    k = 0
    c = 0.0
    while (np.abs(a - b) >= tol) and k < maxiter:

        c = (a + b) / 2.0
        left = (a + c) / 2.0
        right = (c + b) / 2.0
        fl = f(left)
        fr = f(right)
        if fr > fl:
            b = right
        elif fl > fr:
            a = left
        else:
            a = left
            b = right
        k += 1
    print("Total no. of iterations to find the minimum of the Obj func = ", k)
    print("The minimum point is = ", round(c, 4))
    print("The minimum F(x) = ", round(f(c), 4))

    return round(c, 4), k


def myplot(c, f):

    m = np.linspace(-10, 10, 1000)
    fv = []
    for i in range(len(m)):
        fv.append(f(m[i]))

    plt.figure()
    plt.plot(m, fv, color="red", linewidth=2)
    plt.scatter(c, f(c), color="b", marker='o')
    plt.title("F(x) minimization using bisection method", fontsize=24)
    plt.legend(("F(x)", "Minimum"), fontsize=14)
    plt.xlabel("x", fontsize=24)
    plt.ylabel("F(x)", fontsize=24)
    plt.xlim(-10, 10)
    plt.grid()
    plt.axes().axhline(y=0, color='k')
    plt.axes().axvline(x=0, color='k')

    return plt.show()


if __name__ == "__main__":

    func = lambda x: x**3 - 3*x**2
    A = 0.9
    B = 3.0
    tolerance = 1e-6
    maxiteration = 1e3
    C, K=bisection(func, A, B, tolerance, maxiteration)
    print(C, K)
    myplot(C, func)
