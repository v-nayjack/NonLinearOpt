# Created by Vinay Jakkali on 12/12/2019

"""
--------------------------------------------------------------------------------------
Problem 6 calculations for the various input points to find the optimized robot
path
--------------------------------------------------------------------------------------
"""

import numpy as np
import TwoStageRouting as Routing
from MonteCarlo import monte_carlo
from BasinHopping import basin_hopping
from ParticleSwarm import particle_swarm



if __name__ == '__main__':

    # Input Values for the 'routing' function
    Point = np.array([3, 3])
    Center = np.array([2, 2])
    Radius = 1
    Rho = 100
    X0 = np.array([2, 1])
    tolerance = 1e-8

    Func = lambda x: Routing.routing_two(x, Point, Center, Radius, Rho)

    # Returned Values
    IntermediatePnt_BH = basin_hopping(Func, X0, 1)


    # Robot Path Plot
    Routing.routing_plot(Center, Radius, Point, np.around(IntermediatePnt_BH, decimals=2))

    # Results output printed to the console
    print(" The intermediate point is = ", np.around(IntermediatePnt_BH, decimals=2))
    print(" The minimum F(x) = ", round(Func(IntermediatePnt_BH), 4))

