import matplotlib.pyplot as plt
from univariate import univariatescan as interval
from bisection import bisection as bisect


def routing(p=(5.0, 3.0), cent=(2.0, 2.0), r=1.0, rho=20, x0=10, tol=1e-8):
    """ The routing function defined here takes following parameters as input
    INPUT:
    p : it is a tuple that takes target point coordinates as input P(x.0,y.0)
    cent: it is a tuple that takes the center of the circle as input C(x.0,y.0)
    r : it is the radius of the circle and takes float value as input
    rho : it the penalty term
    x0 : it is initial guess required for univariate scan to bracket the interval
    tol : This is the tolerance accepted for the minimized objective function

    OUTPUT:
    Plots showing bracketed interval, objective function with the minimum point and the optimized robot path
    Also prints the values of minimum x, minimum F(x) to the console"""

    aa = lambda x: (x - p[0])**2 + (p[1])**2
    bb = lambda x: 2*((p[0] - x)*(x - cent[0]) - (p[1]*cent[1]))
    cc = lambda x: (x - cent[0])**2 + (cent[1])**2 - r**2
    delta = lambda x: bb(x)**2 - 4*aa(x)*cc(x)
    f = lambda x: (x + ((aa(x)) ** 0.5) * (1 + rho * abs((((delta(x)) ** 0.5) / (aa(x)))))) if delta(x) > 0 else x + (
                (aa(x)) ** 0.5)
    [a, b, k] = interval(f, x0)
    minimum, ok = bisect(f, a, b, tol)
    print("The minimum distance on x axis = ", round(minimum, 4))
    print("The minimum F(x) =", round(f(minimum), 4))
    circle = plt.Circle(cent, r, color='b', fill=False)
    plt.gcf().gca().add_artist(circle)
    plt.scatter(cent[0], cent[1], color='r', marker='*')
    plt.scatter(0, 0, color='g', marker='x')
    plt.scatter(minimum, 0, color='r', marker='x')
    plt.scatter(p[0], p[1], color='b', marker='o')
    plt.plot([0, minimum], [0, 0], color='r')
    plt.plot([minimum, p[0]], [0, p[1]], color='k')
    plt.title('Optimal Robot Path', fontsize=24)
    plt.xlabel('x axis', fontsize=24)
    plt.ylabel('y axis', fontsize=24)
    plt.xlim(0, 5.5)
    plt.ylim(-0.5, 5.5)
    plt.grid()
    # plt.axes().set_aspect('equal')
    plt.axes().axhline(y=0, color='g')
    plt.axes().axvline(x=0, color='k')
    plt.show()

    
routing(p=(2.0, 5.0), cent=(2.0, 2.0), r=1.0, rho=20, x0=0.5, tol=1e-8)
