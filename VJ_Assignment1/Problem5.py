# Created by Vinay Jakkali on 11/25/2019

"""
--------------------------------------------------------------------------------------
The routing function defined here takes following parameters as input

INPUT:
    p : it is a tuple that takes target point coordinates as input P(x.0,y.0)
    (by default p = (5.0, 3.0))

    center: it is a tuple that takes the center of the circle as input C(x.0,y.0)
    (by default center = (2.0, 2.0))

    r : it is the radius of the circle and takes float value as input
    (by default r = 1.0)

    rho : it the penalty term
    (by default rho = 20)

    x0 : it is initial guess required for univariate scan to bracket the interval
    (by default x0 = 10.0)

    tol : This is the tolerance accepted for the minimized objective function
    (by default tol = 1e-8)

OUTPUT:
    1. A new window with the plot showing bracketed interval, objective function with the minimum point and the
    optimized robot path.

    2. Print the values of total number of iterations 'k', minimum 'x', minimum 'F(x)' to the console
--------------------------------------------------------------------------------------
"""

import matplotlib.pyplot as plt
from UnivariateMethod import univariatescan as interval
from BisectionMethod import bisection as bisect
from UnivariateMethod import univariate_plot as u_plt
from BisectionMethod import bisection_plot as bi_plt

def routing(p=(5.0, 3.0), center=(2.0, 2.0), r=1.0, rho=20, x0=10.0, tol=1e-8):

    aa = lambda x: (x - p[0]) ** 2 + (p[1]) ** 2

    bb = lambda x: 2 * ((p[0] - x) * (x - center[0]) - (p[1] * center[1]))

    cc = lambda x: (x - center[0]) ** 2 + (center[1]) ** 2 - r ** 2

    delta = lambda x: bb(x) ** 2 - 4 * aa(x) * cc(x)

    f = lambda x: (x + ((aa(x)) ** 0.5) * (1 + rho * abs((((delta(x)) ** 0.5) / (aa(x)))))) \
        if delta(x) > 0 else x + ((aa(x)) ** 0.5)

    a, b, iter_uni = interval(f, x0)

    minimum, iter_bi = bisect(f, a, b, tol)

    return round(a, 4), round(b, 4), round(minimum, 4), f

""" Function 'routing_plot' plots the robot path along with the given circle """

def routing_plot(center, r, p, minimum):

    plt.figure()
    circle = plt.Circle(center, r, color='b', fill=False)
    plt.gcf().gca().add_artist(circle)
    plt.scatter(center[0], center[1], color='r', marker='*')
    plt.scatter(0, 0, color='g', marker='x')
    plt.scatter(minimum, 0, color='r', marker='x')
    plt.scatter(p[0], p[1], color='b', marker='o')
    plt.plot([0, minimum], [0, 0], color='r')
    plt.plot([minimum, p[0]], [0, p[1]], color='k')
    plt.title('Optimal Robot Path', fontsize=20)
    plt.xlabel('x axis', fontsize=16)
    plt.ylabel('y axis', fontsize=16)
    plt.xlim(0, 5.5)
    plt.ylim(-0.5, 5.5)
    plt.grid(True)
    plt.axes().axhline(y=0, color='g')
    plt.axes().axvline(x=0, color='k')
    plt.axes().set_aspect('equal')

    return plt.show()


if __name__ == "__main__":

    # Input Values for the 'routing' function
    Point = (1.0, 3.0)
    Center = (2.0, 2.0)
    Radius = 1.0
    Rho = 20
    X0 = 0.5
    tolerance = 1e-8

    # Returned Values
    A, B, Minimum, Func = routing(Point, Center, Radius, Rho, X0, tolerance)

    # Objective Function Plot
    u_plt(A, B, Func)

    # Objective Function Plot
    bi_plt(Minimum, Func)

    # Robot Path Plot
    routing_plot(Center, Radius, Point, Minimum)

    # Results output printed to the console
    print(" The minimum distance on x axis = ", Minimum)
    print(" The minimum F(x) = ", round(Func(Minimum), 4))
