# Created by Vinay Jakkali on 12/8/2019

"""
--------------------------------------------------------------------------------------
Include code description here:

--------------------------------------------------------------------------------------
"""

import numpy as np
from Quasi_Newton import quasi_newton
from PowellMethod import powell_method

def rosenbrock(x0):

    N = len(x0)
    F =


    for i in range(N-1):

        Sigma_F = lambda x: (100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2)

        F += Sigma_F

    return F

if __name__ == "__main__":

    X0 = np.array([2.55, 1.75])

    L = np.array([0, 0.])

    U = np.array([10., 10.])

    Func = rosenbrock(X0)
    print("Function", Func)

    QN_minX, QN_H_K, QN_K = quasi_newton(Func, X0)

    P_minX, P_K = powell_method(Func, X0, L, U)

    print("Quasi Newton Minimum  ", QN_minX)
    print('Quasi Newton Fmin', Func(QN_minX))
    print("Quasi Newton total no. of iterations = ", QN_K)

    print("Powell Method Minimum  ", P_minX)
    print('Powell Method Fmin', Func(P_minX))
    print("Powell Method total no. of iterations = ", P_K)
