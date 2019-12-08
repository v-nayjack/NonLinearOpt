# Created by Vinay Jakkali on 11/26/2019

"""
--------------------------------------------------------------------------------------
Include code description here:

--------------------------------------------------------------------------------------
"""

import numpy as np
from BisectionMethod import bisection


def powell_method(F, x0, Left, Right, maxiter=1e5, tol=1e-8):

    X_k = np.copy(x0)  # 1xN


    N = len(x0)  # Scalar
    D = np.ones(N)  # NxN

    S_star = np.zeros(N)
    k = 0
    stop_criteria = 1.0

    while stop_criteria > tol and k < maxiter:

    #   print("iteration =", k)

        for i in range(N):

            f = lambda s: F(X_k +(s*D))  # 1xN

#            print("X_k = ", X_k)

            a = Left[i] - X_k[i]
            b = Right[i] - X_k[i]

#            print('a', a)
#            print('b', b)

            S = bisection(f, a, b)  # Scalar
#            print('S', S)

            S_star[i] = S  # Nx1

#        print('S_star', S_star)
        X_k1 = X_k + (S_star * D)
#        print('X_k1', X_k1)

        i_star = np.argmax(abs(S_star * D))  # Scalar
#        print('index', i_star)

        D[i_star] = X_k1[i_star] - X_k[i_star]  # 1xN
#        print('D', D)

        stop_criteria = np.linalg.norm(X_k1 - X_k)
#        print(stop_criteria)

        X_k = X_k1

        k += 1

    return X_k1, k


if __name__ == "__main__":

    Func = lambda x: -4*x[0] + x[0]**2 - x[1] - x[0]*x[1] + x[1]**2

    X0 = np.array([-1.0, 6.8])

    L = np.array([0, 0.])

    U = np.array([10., 10.])

    minX, K = powell_method(Func, X0, L, U)

    print("minimum exists at  ", minX)
    print('Fmin', Func(minX))
    print("total no. of iterations = ", K)


    
























