# Created by Vinay Jakkali on 12/8/2019

"""
--------------------------------------------------------------------------------------
The quasi_newton function defined here takes following parameters as input

INPUT:
    F : It is the objective function

    x0 : It is an array of size Nx1 initial guesses required for Quasi-Newton method

    tol : This is the tolerance accepted for the minimized objective function
    (by default tol = 1e-8)

    maxiter : Maximum iterations to stop the optimization
    (by default maxiter = 1e3)

OUTPUT:
    1. Returns the values of minimum 'X_k' and total number of iterations 'k'
--------------------------------------------------------------------------------------
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
from ArmijoLineSearch import armijolinesearch as als
from BFGS import bfgs
from Gradient import gradient as grad


def quasi_newton(F, x0, tol=1e-8, maxiter=1e5):

    X_k = np.copy(x0)

    N = len(X_k)

    H0 = np.identity(N)  # Initial guess for approximation of the inverse of the Hessian

    H_k = np.copy(H0)

    k = 0

    stop_criteria = 1.0

    while stop_criteria > tol and k < maxiter:

        G_k = grad(F, X_k)  # Gradient vector of F at X_k

        P_k = np.dot(-H_k, G_k)  # Direction vector

        S = als(F, X_k, P_k)  # Step size obtained from weak line search

        X_k1 = X_k + S * P_k.flatten()  # Updated X values

        Delta_k = S * P_k  # Delta vector

        G_k1 = grad(F, X_k1)  # Gradient vector of F at X_k1

        Gamma_k = G_k1 - G_k  # Gamma vector containing differences of gradients at X_k1 and X_k

        H_k1 = bfgs(H_k, Gamma_k, Delta_k)  # BFGS update for H(k+1)

        X_k = X_k1

        H_k = H_k1

        stop_criteria = np.linalg.norm(G_k)


        k += 1

    return np.around(X_k, decimals=2), k


def quasi_newton_surfaceplot(f, xmin):

    """ Creating points for plotting the objective function """

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Creating Data points for surface plot

    xlist = np.linspace(-5, 5, 1000)
    ylist = np.linspace(-5, 5, 1000)

    X, Y = np.meshgrid(xlist, ylist)
    Z = f([X, Y])

    # Plotting the Surface
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    # Plotting the minimums on the plot surface
    ax.scatter(xmin[0], xmin[1], f(xmin), color='red', marker='*')

    # Customizing the Objective Function axis (z-axis)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Adding the color bar
    fig.colorbar(surf)

    # Adding the title and axes labels
    ax.set_title("F(x) minimization using Quasi-Newton Method")
    ax.set_xlabel(" x-axis ")
    ax.set_ylabel(" y-axis ")
    ax.set_zlabel(" F(x) ")

    return plt.show()


def quasi_newton_contourplot(f, xmin):

    """ Creating points for plotting the objective function """

    fig = plt.figure()
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    ax = fig.add_axes([left, bottom, width, height])

    # Creating Data points for contour plot

    xlist = np.linspace(-5, 5, 1000)
    ylist = np.linspace(-5, 5, 1000)

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
    ax.set_title("F(x) minimization using Quasi-Newton Method")
    ax.set_xlabel(" x-axis ")
    ax.set_ylabel(" y-axis ")

    return plt.show()


if __name__ == "__main__":

    Func = lambda x: -4*x[0] + x[0]**2 - x[1] - x[0]*x[1] + x[1]**2

    X0 = np.array([2.55, 1.75])

    minX, K = quasi_newton(Func, X0)

    quasi_newton_surfaceplot(Func, minX)
    quasi_newton_contourplot(Func, minX)

    print("minimum exists at  ", minX)
    print('Fmin', Func(minX))
    print("total no. of iterations = ", K)



