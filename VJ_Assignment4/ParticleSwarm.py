# Created by Vinay Jakkali on 12/12/2019

"""
--------------------------------------------------------------------------------------
Include code description here:

--------------------------------------------------------------------------------------
"""
import numpy as np
from Rosenbrock import rosenbrock

def particle_swarm(F, Dims, Particles, Inertia, phip, phig, L, U, maxiter=1e3):

    Low = np.full(Dims, L)
    Up = np.full(Dims, U)

    SearchGrid = np.hstack((Low, Up))

    X0 = np.zeros((Particles, Dims))
    V0 = np.zeros((Particles, Dims))

    for i in range(Dims):

        X0[:, i] = (SearchGrid[i+Dims] - SearchGrid[i]) * np.random.rand(Particles) + SearchGrid[i]

        V0[:, i] = np.random.rand(Particles)

    X_local = X0
    F_IP = np.zeros(Particles)

    for i in range(Particles):

        F_IP[i] = F(X_local[i, :])

    index = np.argmin(F_IP)

    X_global = X_local[index, :]

    k = 0

    while k < maxiter:

        for i in range(Particles):

            V0[i, :] = Inertia * V0[i, :] + phip * np.random.rand(1) * (X_local[i, :] - X0[i, :]) + \
                phig * np.random.rand(1) * (X_global - X0[i, :])

            X0[i, :] = X0[i, :] + V0[i, :]

            if F(X0[i, :]) < F(X_local[i, :]):

                X_local[i, :] = X0[i, :]

                F_IP[i] = F(X_local[i, :])

        index = np.argmin(F_IP)

        X_global = X_local[index, :]

        k += 1

    Xk_min = X_global

    return Xk_min


if __name__ == "__main__":


    xmin = particle_swarm(rosenbrock, 5, 500, 0.5, 2, 2, 0, 2)

    print("Xmin", xmin)

