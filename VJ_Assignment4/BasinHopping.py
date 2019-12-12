# Created by Vinay Jakkali on 12/12/2019

"""
--------------------------------------------------------------------------------------
Include code description here:

--------------------------------------------------------------------------------------
"""
import numpy as np
import math as m
from scipy.optimize import minimize
from Rosenbrock import rosenbrock

def basin_hopping(F, x0, T=1, maxiter=1e3):
    X0 = np.copy(x0)
    res = minimize(F, X0, method='Powell', options={'xtol': 1e-8, 'disp': False})
    Z0 = res.x  # local minimum based on the initial guess X0
    Tmin = 1e-8  # minimum temperature
    k = 0

    while k < maxiter:

        X_star = X0 + 0.01 * np.random.rand(1)

        res = minimize(F, X_star, method='Powell', options={'xtol': 1e-8, 'disp': False})

        Z_star = res.x

        P = np.exp((-(F(Z_star) - F(Z0)) / T))  # acceptance probability

        if np.random.rand(1) <= P:

            X0 = X_star
            Z0 = Z_star

        T = T * 0.95**k  # Temperature update

        if T <= Tmin:
            return Z0

        k += 1

    return Z_star


if __name__ == "__main__":

    iniX = np.array([2., 3., 4., 5., 6.])


    xmin = basin_hopping(rosenbrock, iniX, 1)

    print("Xmin", xmin)








