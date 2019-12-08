# Created by Vinay Jakkali on 12/8/2019

"""
--------------------------------------------------------------------------------------
Include code description here:

--------------------------------------------------------------------------------------
"""

import numpy as np

def gradient(F, x0, tol=1e-8):

    initialX = np.copy(x0)
    #print("X0", initialX)

    N = len(initialX)
    #print("N", N)

    h = np.eye(N)

    h = h * tol

    #print("h", h)

    g = np.zeros(N)
    #print("g", g)

    for i in range(N):

        H = np.copy(h[i, :])

        g[i] = (F(x0 + H) - F(x0 - H))/(2*tol)

    return g


if __name__ == "__main__":


    Func = lambda x: (x[0] - 1) ** 2 + x[1] ** 3 - x[0] * x[1]

    X0 = np.array([7.8, 1.5])

    Gradient = gradient(Func, X0)

    print("Gradient", Gradient)

