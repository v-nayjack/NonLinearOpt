# Created by Vinay Jakkali on 11/26/2019

"""
--------------------------------------------------------------------------------------
The powell_method function defined here takes following parameters as input

INPUT:
    F : It is the objective function

    x0 : It is an array of size Nx1 initial guesses required for Powell's method

    Lower: It is an array of size Nx1 lower bound values

    Upper: It is an array of size Nx1 upper bound values

    tol : This is the tolerance accepted for the minimized objective function
    (by default tol = 1e-8)

    maxiter : Maximum iterations to stop the optimization
    (by default maxiter = 1e3)

OUTPUT:
    1. Returns the values of minimum 'X_k' and total number of iterations 'k'
--------------------------------------------------------------------------------------
"""

import numpy as np
from BisectionMethod import bisection


def powell_method(F, x0, Lower, Upper, maxiter=1e5, tol=1e-8):

    X_k = np.copy(x0)  # 1xN

    N = len(x0)  # Scalar

    D = np.ones(N)  # NxN

    S_star = np.zeros(N)

    k = 0

    stop_criteria = 1.0

    while stop_criteria > tol and k < maxiter:


        for i in range(N):

            f = lambda s: F(X_k +(s*D))  # 1xN

            a = Lower[i] - X_k[i]
            b = Upper[i] - X_k[i]

            S = bisection(f, a, b)  # Scalar

            S_star[i] = S  # Nx1

        X_k1 = X_k + (S_star * D)

        i_star = np.argmax(abs(S_star * D))  # Scalar

        D[i_star] = X_k1[i_star] - X_k[i_star]  # 1xN

        stop_criteria = np.linalg.norm(X_k1 - X_k)

        X_k = X_k1

        k += 1

    return np.around(X_k, decimals=2), k


if __name__ == "__main__":

    Func = lambda x: -4*x[0] + x[0]**2 - x[1] - x[0]*x[1] + x[1]**2

    X0 = np.array([-1.0, 6.8])

    L = np.array([0, 0.])

    U = np.array([10., 10.])

    minX, K = powell_method(Func, X0, L, U)

    print("minimum exists at  ", minX)
    print('Fmin', Func(minX))
    print("total no. of iterations = ", K)


    

























