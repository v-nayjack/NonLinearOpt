# Created by Vinay Jakkali on 12/10/2019

"""
--------------------------------------------------------------------------------------
Problem 6 calculations for the various input points to find the optimized robot
path
--------------------------------------------------------------------------------------
"""
import numpy as np
import TwoStageRouting as Routing
from Quasi_Newton import quasi_newton, quasi_newton_surfaceplot, quasi_newton_contourplot



if __name__ == '__main__':

    # Input Values for the 'routing' function
    Point = (3.0, 3.0)

    Center = (2.0, 2.0)

    Radius = 1.0

    Rho = 50

    X0 = np.array([2., 1.])

    tolerance = 1e-8

    Func = lambda x: Routing.routing_two(x, Point, Center, Radius, Rho)

    # Returned Values
    IntermediatePnt, k = quasi_newton(Func, X0)


    # Robot Path Plot
    Routing.routing_plot(Center, Radius, Point, IntermediatePnt)

    # Results output printed to the console
    print(" The intermediate point is = ", IntermediatePnt)
    print(" The minimum F(x) = ", Func(IntermediatePnt))







