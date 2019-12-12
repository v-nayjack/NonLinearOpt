# Created by Vinay Jakkali on 12/12/2019

"""
--------------------------------------------------------------------------------------
Include code description here:

--------------------------------------------------------------------------------------
"""
import numpy as np
from Ackley import ackley
from MonteCarlo import monte_carlo
from BasinHopping import basin_hopping
from ParticleSwarm import particle_swarm

def main():

    """ Finding the global minimum for Ackley function using Monte Carlo, Basin Hopping and Particle Swarm methods """

    """ Monte Carlo Method """

    Xmin_MC = monte_carlo(ackley, 500, 2, 0, 2)

    """ Basin Hopping Method """

    X0 = np.array([0.5, 0.5])

    Xmin_BH = basin_hopping(ackley, X0, 1)

    """ Particle Swarm Method """

    Xmin_PS = particle_swarm(ackley, 2, 500, 0.5, 2, 2, 0, 2)

    return Xmin_MC, Xmin_BH, Xmin_PS


if __name__ == "__main__":

    MC, BH, PS = main()

    print("Monte Carlo Minimization of Ackley Function ", np.around(MC, decimals=4))
    print("Basin Hopping Minimization of Ackley Function ", np.around(BH, decimals=4))
    print("Particle Swarm Minimization of Ackley Function ", np.around(PS, decimals=4))

