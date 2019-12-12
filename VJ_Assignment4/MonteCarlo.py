# Created by Vinay Jakkali on 12/12/2019

"""
--------------------------------------------------------------------------------------
Include code description here:

--------------------------------------------------------------------------------------
"""

import numpy as np
from scipy.optimize import minimize
from Rosenbrock import rosenbrock


def monte_carlo(F, N, Dims, L, U):

    Low = np.full(Dims, L)
    Up = np.full(Dims, U)

    SearchGrid = np.hstack((Low, Up))

    Input_points = np.zeros((N, Dims))

    for i in range(Dims):

        Input_points[:, i] = (SearchGrid[i+Dims] - SearchGrid[i]) * np.random.rand(N) + SearchGrid[i]

    F_IP = np.zeros(N)

    for i in range(N):

        F_IP[i] = F(Input_points[i, :])

    index = np.argmin(F_IP)

    Xk_min = Input_points[index, :]

    res = minimize(F, Xk_min, method='Powell', options={'xtol': 1e-8, 'disp': False})

    X_min = res.x

    return X_min


if __name__ == "__main__":


    xmin = monte_carlo(rosenbrock, 500, 5, -10, 10)

    print("Xmin", xmin)
