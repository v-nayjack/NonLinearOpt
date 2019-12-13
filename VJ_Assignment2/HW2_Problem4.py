# Created by Vinay Jakkali on 12/9/2019

"""
--------------------------------------------------------------------------------------
Problem 4 calculations to minimize the give two dimensional function using Powell's
Method or Quasi-Newton Method
--------------------------------------------------------------------------------------
"""
import numpy as np
from Quasi_Newton import quasi_newton, quasi_newton_surfaceplot, quasi_newton_contourplot

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D


def f(x):

    F = (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

    return F


def main():

    Fmins = lambda x: f(x)

    Fmaxs = lambda x: -1 * f(x)

    X0 = np.array([[-5., -2.], [5., -2.5], [-3., 3.8], [4.75, 1.8], [3., 2.]])

    Minimums = np.zeros(np.shape(X0))

    Maximums = np.zeros(np.shape(X0))

    F_mins = np.zeros(len(X0))

    F_maxs = np.zeros(len(X0))

    for i in range(len(X0)):

        Minimums[i, :], k1 = quasi_newton(Fmins, X0[i, :])

        F_mins[i] = Fmins(Minimums[i, :])

        Maximums[i, :], k2 = quasi_newton(Fmaxs, X0[i, :])

        F_maxs[i] = Fmaxs(Maximums[i, :])

    return np.around(Minimums, decimals=2), np.around(Maximums, decimals=2), F_mins, F_maxs






if __name__ == '__main__':

    Mins, Maxs, f_mins, f_maxs = main()


    TotalMins = np.unique(f_mins)

    TotalMaxs = np.where(np.unique(f_maxs >= 0.))[0]


    """ Creating points for plotting the objective function """

    fig = plt.figure()
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    ax = fig.add_axes([left, bottom, width, height])

    # Creating Data points for contour plot

    xlist = np.linspace(-5, 5, 100)
    ylist = np.linspace(-5, 5, 100)

    X, Y = np.meshgrid(xlist, ylist)
    Z = f([X, Y])

    # Plotting the contour
    cp = plt.contourf(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    # Plotting the minimums on the plot surface
    plt.scatter(Mins[:, 0], Mins[:, 1], color='red', marker='*')
#    plt.scatter(Maxs[4, 0], Maxs[4, 1], color='black', marker='o')

    # Annotating the local minimum
#    ax.annotate('local min', xy=(xmin[0], xmin[1]), xytext=(xmin[0]+0.5, xmin[1]+0.5), fontsize=12,
#                ha='center', va='top')

    # Adding the color bar
    plt.colorbar(cp)


    # Adding the title and axes labels
    ax.set_title(" Local Minimums")
    ax.set_xlabel(" x-axis ")
    ax.set_ylabel(" y-axis ")

    plt.show()

#    quasi_newton_contourplot(f, Mins[0, :])
#    quasi_newton_surfaceplot(f, Mins[0, :])


    print("Minimums", Mins)
    print("Maximums", Maxs)
    print("Fmins", f_mins)
    print("Fmaxs", f_maxs)

    print("Total no. of minimums", len(TotalMins))
    print("Total no. of maximums", len(TotalMaxs))




