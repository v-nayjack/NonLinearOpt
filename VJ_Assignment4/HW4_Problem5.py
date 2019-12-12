# Created by Vinay Jakkali on 12/12/2019

"""
--------------------------------------------------------------------------------------
Problem 5 calculations to minimize Rosenbrock Function using Monte Carlo, Basin Hopping
and Particle Swarm optimization methods
--------------------------------------------------------------------------------------
"""
import numpy as np
from Rosenbrock import rosenbrock
from MonteCarlo import monte_carlo
from BasinHopping import basin_hopping
from ParticleSwarm import particle_swarm

def main():

    """ Finding the global minimum for Ackley function using Monte Carlo, Basin Hopping and Particle Swarm methods """

    """ Monte Carlo Method """

    Xmin_MC = monte_carlo(rosenbrock, 500, 5, -10, 10)

    """ Basin Hopping Method """

    X0 = np.array([2., 3., 4., 5., 6.])

    Xmin_BH = basin_hopping(rosenbrock, X0, 1)

    """ Particle Swarm Method """

    Xmin_PS = particle_swarm(rosenbrock, 5, 500, 0.5, 2, 2, -10, 10)

    return Xmin_MC, Xmin_BH, Xmin_PS


if __name__ == "__main__":

    MC, BH, PS = main()

    print("Monte Carlo Minimization of Rosenbrock Function ", np.around(MC, decimals=4))
    print("Basin Hopping Minimization of Rosenbrock Function ", np.around(BH, decimals=4))
    print("Particle Swarm Minimization of Rosenbrock Function ", np.around(PS, decimals=4))