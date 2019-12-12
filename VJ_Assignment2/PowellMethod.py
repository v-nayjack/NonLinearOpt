# Created by Vinay Jakkali on 11/26/2019

"""
--------------------------------------------------------------------------------------
The powell_method function defined here takes following parameters as input

INPUT:
    F : It is the objective function

    x0 : It is an array of size Nx1 initial guesses required for Powell's method

    Lower: It is an array of size Nx1 lower bound values

    Upper: It is an array of size Nx1 upper bound values

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
from BisectionMethod import bisection


def powell_method(F, x0, Lower, Upper, maxiter=1e5, tol=1e-8):

    X_k = np.copy(x0)  # 1xN

    N = len(x0)  # Scalar

    D = np.ones(N)  # NxN

    S_star = np.zeros(N)

    k = 0

    stop_criteria = 1.0

    while stop_criteria > tol and k < maxiter:


        for i in range(N):

            f = lambda s: F(X_k +(s*D))  # 1xN

            a = Lower[i] - X_k[i]
            b = Upper[i] - X_k[i]

            S = bisection(f, a, b)  # Scalar

            S_star[i] = S  # Nx1

        X_k1 = X_k + (S_star * D)

        i_star = np.argmax(abs(S_star * D))  # Scalar

        D[i_star] = X_k1[i_star] - X_k[i_star]  # 1xN

        stop_criteria = np.linalg.norm(X_k1 - X_k)

        X_k = X_k1

        k += 1

    return np.around(X_k, decimals=2), k


def powell_surfaceplot(f, xmin):

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
    ax.set_title("F(x) minimization using Powell's Method")
    ax.set_xlabel(" x-axis ")
    ax.set_ylabel(" y-axis ")
    ax.set_zlabel(" F(x) ")

    return plt.show()


def powell_contourplot(f, xmin):

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
    ax.set_title("F(x) minimization using Powell's Method")
    ax.set_xlabel(" x-axis ")
    ax.set_ylabel(" y-axis ")

    return plt.show()


if __name__ == "__main__":

    Func = lambda x: -4*x[0] + x[0]**2 - x[1] - x[0]*x[1] + x[1]**2

    X0 = np.array([-1.0, 6.8])

    L = np.array([0, 0.])

    U = np.array([10., 10.])

    minX, K = powell_method(Func, X0, L, U)

    powell_surfaceplot(Func, minX)
    powell_contourplot(Func, minX)

    print("minimum exists at  ", minX)
    print('Fmin', Func(minX))
    print("total no. of iterations = ", K)


    

























