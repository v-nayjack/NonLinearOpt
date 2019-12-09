# Created by Vinay Jakkali on 12/8/2019

"""
--------------------------------------------------------------------------------------
Include code description here:

--------------------------------------------------------------------------------------
"""

import numpy as np
from ArmijoLineSearch import armijolinesearch as als
from BFGS import bfgs
from Gradient import gradient as grad


def quasi_newton(F, x0, tol=1e-8, maxiter=1e5):

    X_k = np.copy(x0)

    N = len(X_k)

    H0 = np.identity(N)

    H_k = np.copy(H0)

    k = 0

    stop_criteria = 1.0

    while stop_criteria > tol and k < maxiter:

        G_k = grad(F, X_k)
        print("G_k", G_k)

        P_k = np.dot(-H_k, G_k)
        print("P_k", P_k)

        S = als(F, X_k, P_k)
        print("S", S)

        X_k1 = X_k + S * P_k.flatten()
        print("X_k1", X_k1)
        print("X_k", X_k)

        Delta_k = S * P_k
        print("Delta_k", Delta_k)

        G_k1 = grad(F, X_k1)
        print("G_k1", G_k1)

        Gamma_k = G_k1 - G_k
        print("Gamma_k", Gamma_k)

        Hk_1 = bfgs(H_k, Gamma_k, Delta_k)
        print("H_k1", Hk_1)

        X_k = X_k1

        H_k = Hk_1

        stop_criteria = np.linalg.norm(G_k)
        print("Stopping Criteria", stop_criteria)

        k += 1

    return X_k, H_k, k


if __name__ == "__main__":

    Func = lambda x: -4*x[0] + x[0]**2 - x[1] - x[0]*x[1] + x[1]**2

    X0 = np.array([2.55, 1.75])

    minX, H_K, K = quasi_newton(Func, X0)

    print("minimum exists at  ", minX)
    print('Fmin', Func(minX))
    print("total no. of iterations = ", K)



