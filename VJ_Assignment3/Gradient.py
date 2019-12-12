# Created by Vinay Jakkali on 12/8/2019

"""
--------------------------------------------------------------------------------------
Include code description here:

--------------------------------------------------------------------------------------
"""

import numpy as np

def gradient(F, x0, tol=1e-8):

    X_k = np.copy(x0)


    N = len(X_k)


    h = np.eye(N)

    h = h * tol



    g = np.zeros(N, )



    for i in range(N):

        H = np.copy(h[i, :])

        g[i] = (F(X_k + H) - F(X_k - H))/(2*tol)

    g = g[:, np.newaxis]

    return g


if __name__ == "__main__":


    Func = lambda x: (x[0] - 1) ** 2 + x[1] ** 3 - x[0] * x[1]

    X0 = np.array([7.8, 1.5])

    Gradient = gradient(Func, X0)

    print("Gradient", Gradient)

