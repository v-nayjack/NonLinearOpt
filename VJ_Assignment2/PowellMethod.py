# Created by Vinay Jakkali on 11/26/2019

"""
--------------------------------------------------------------------------------------
Include code description here:

--------------------------------------------------------------------------------------
"""

import numpy as np
from UnivariateMethod import univariatescan
from BisectionMethod import bisection


def powell_method(F, x0, maxiter=1e5, tol=1e-8):

    X_k = x0  # 1xN
    X_k1 = x0  # 1xN


    N = len(x0)  # Scalar
    D = np.eye(N)  # NxN
    Z = []
    SuccDir = []
    S_star = []
    k = 0

    while (np.linalg.norm(X_k1 - X_k) < tol) and k < maxiter:

        Z = X_k1  # 1xN

        for i in range(N):

            f = lambda s: F(Z + s * D[i, :])  # 1xN

            a, b = univariatescan(f, Z[i])  # Scalar

            S = bisection(f, a, b)  # Scalar

            Z = Z + S * D[i, :]  # 1xN

            S_star.append(S)  # Nx1

            Si_Di = np.linalg.norm(S * D[i, :])  # Scalar

            SuccDir.append(Si_Di)  # Nx1

        ind = np.argmax(SuccDir)  # Scalar

        D[ind, :] = Z - X_k  # 1xN

        X_k1 = Z

        k += 1

        return X_k1, k

    

























