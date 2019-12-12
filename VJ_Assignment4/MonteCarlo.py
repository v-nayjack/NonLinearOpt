# Created by Vinay Jakkali on 12/12/2019

"""
--------------------------------------------------------------------------------------
The particle_swarm function defined here takes following parameters as input

INPUT:
    F : It is the objective function

    N : It is the total # of random points

    Dims : It is the total # of dimensions

    L : Lower bound of the search space

    U : Upper bound of the search space

OUTPUT:
    1. Returns the values of minimum 'Xk_min'
--------------------------------------------------------------------------------------
"""

import numpy as np
from scipy.optimize import minimize
from Rosenbrock import rosenbrock


def monte_carlo(F, N, Dims, L, U):

    """ Monte Carlo Optimization of the given objective function"""

    """ Creating the search space """

    Low = np.full(Dims, L)

    Up = np.full(Dims, U)

    SearchGrid = np.hstack((Low, Up))

    """ Initializing input points """

    Input_points = np.zeros((N, Dims))

    for i in range(Dims):

        """ Randomly Initializing input points """

        Input_points[:, i] = (SearchGrid[i+Dims] - SearchGrid[i]) * np.random.rand(N) + SearchGrid[i]

    F_IP = np.zeros(N)  # Initializing objective at each input point

    for i in range(N):

        F_IP[i] = F(Input_points[i, :])  # Computing objective at each input point

    index = np.argmin(F_IP)  # Finding the point with smallest objective value

    Xk_min = Input_points[index, :]  # Setting this as minimum point

    res = minimize(F, Xk_min, method='Powell', options={'xtol': 1e-8, 'disp': False})

    X_min = res.x  # Updating the input points based on minimization

    return X_min


if __name__ == "__main__":


    xmin = monte_carlo(rosenbrock, 500, 5, -10, 10)

    print("Xmin", xmin)
