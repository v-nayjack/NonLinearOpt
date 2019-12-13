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

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

def basinhopping_contourplot(f, xmin):

    """ Creating points for plotting the objective function """

    fig = plt.figure()
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    ax = fig.add_axes([left, bottom, width, height])

    # Creating Data points for contour plot

    xlist = np.linspace(-5, 5, 10)
    ylist = np.linspace(-5, 5, 10)

    X, Y = np.meshgrid(xlist, ylist)
    Z = f([X, Y])

    # Plotting the contour
    cp = plt.contourf(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    # Plotting the minimums on the plot surface
    plt.scatter(xmin[0], xmin[1], color='red', marker='*')

    # Annotating the local minimum
    ax.annotate('local min', xy=(xmin[0], xmin[1]), xytext=(xmin[0]+0.5, xmin[1]+0.5), fontsize=12,
                ha='center', va='top')

    # Adding the color bar
    plt.colorbar(cp)


    # Adding the title and axes labels
    ax.set_title("Robot path optimization using Basin Hopping Method")
    ax.set_xlabel(" x-axis ")
    ax.set_ylabel(" y-axis ")

    return plt.show()


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

#    basinhopping_contourplot(Func, IntermediatePnt_BH)

    # Results output printed to the console
    print(" The intermediate point is = ", np.around(IntermediatePnt_BH, decimals=2))
    print(" The minimum F(x) = ", round(Func(IntermediatePnt_BH), 4))

