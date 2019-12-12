# Created by Vinay Jakkali on 12/12/2019

"""
--------------------------------------------------------------------------------------
The particle_swarm function defined here takes following parameters as input

INPUT:
    F : It is the objective function

    Dims : It is the total # of dimensions

    Particles : It is the total # of particles

    Omega : Particle Swarms inertial motion

    Phi_p : Movement towards a particle's best known position

    Phi_g : Movement towards a swarm's best known position

    L : Lower bound of the search space

    U : Upper bound of the search space

    maxiter : Maximum iterations to stop the optimization
    (by default maxiter = 1e3)

OUTPUT:
    1. Returns the values of minimum 'Xk_min'
--------------------------------------------------------------------------------------
"""
import numpy as np
from Rosenbrock import rosenbrock

def particle_swarm(F, Dims, Particles, Omega, Phi_p, Phi_g, L, U, maxiter=1e3):

    """ Particle Swarm Optimization for a given objective function """

    """ Creating the search space """

    Low = np.full(Dims, L)

    Up = np.full(Dims, U)

    SearchGrid = np.hstack((Low, Up))

    """ Initializing position and velocity matrices """

    X0 = np.zeros((Particles, Dims))
    V0 = np.zeros((Particles, Dims))

    for i in range(Dims):

        """ Randomly initializing particles' position """

        X0[:, i] = (SearchGrid[i+Dims] - SearchGrid[i]) * np.random.rand(Particles) + SearchGrid[i]

        V0[:, i] = np.random.rand(Particles)  # Randomly initializing each particle with a velocity

    X_local = X0  # Initializing the best known position for each particle

    F_IP = np.zeros(Particles)  # Initializing objective at each particle's position

    for i in range(Particles):

        F_IP[i] = F(X_local[i, :])  # Computing objective at each particle's position

    index = np.argmin(F_IP)  # Finding the particle with smallest objective value

    X_global = X_local[index, :]  # Setting Swarm's best known position

    k = 0

    while k < maxiter:

        for i in range(Particles):

            """ Updating particles' velocity """

            V0[i, :] = Omega * V0[i, :] + Phi_p * np.random.rand(1) * (X_local[i, :] - X0[i, :]) + \
                Phi_g * np.random.rand(1) * (X_global - X0[i, :])

            X0[i, :] = X0[i, :] + V0[i, :]  # Updating particles' position

            if F(X0[i, :]) < F(X_local[i, :]):  # Updating each particles' best known position

                X_local[i, :] = X0[i, :]

                F_IP[i] = F(X_local[i, :])

        index = np.argmin(F_IP)

        X_global = X_local[index, :]  # Updating Swarm's best known position

        k += 1

    Xk_min = X_global

    return Xk_min


if __name__ == "__main__":


    xmin = particle_swarm(rosenbrock, 5, 500, 0.5, 2, 2, 0, 2)

    print("Xmin", xmin)

