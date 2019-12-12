# Created by Vinay Jakkali on 12/10/2019

"""
--------------------------------------------------------------------------------------
Include code description here:

--------------------------------------------------------------------------------------
"""
import numpy as np
import TwoStageRouting as Routing
from Quasi_Newton import quasi_newton
from PowellMethod import powell_method



if __name__ == '__main__':

    # Input Values for the 'routing' function
    Point = (5.0, 3.0)
    Center = (2.0, 2.0)
    Radius = 1.0
    Rho = 20
    X0 = np.array([0., 0.])
    tolerance = 1e-8

    Func = lambda x: Routing.routing_two(x, Point, Center, Radius, Rho)

    # Returned Values
    IntermediatePnt, k = quasi_newton(Func, X0)

    # Robot Path Plot
    Routing.routing_plot(Center, Radius, Point, IntermediatePnt)

    # Results output printed to the console
    print(" The intermediate point is = ", IntermediatePnt)
    print(" The minimum F(x) = ", Func(IntermediatePnt))







