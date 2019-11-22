import numpy as np
import random
from Newton import newton_raphson
import matplotlib.pyplot as plt


def total_least_squares(X0 = 0.1, m = 0.5,N = 100,D_range = (0,5), b = 0.0, eps = 1e-1):
    """Problem 4. function takes the following inputs 
        X0 - It takes a float value, which acts as an initial guess to Newton-Raphson Method
        m - It takes a float value and it represents the slope of the input line
        N - It is the no. of points that are being mapped. It takes an integer value >0
        D_range - It is the range defined for the graph
        b - is the y-intercept and takes a float values
        eps - represents the magnitude of the noise in the input data"""
    R = random.random() # R represents Ri from equation y = mx+b+e(Ri-1)
    x = np.linspace(D_range[0],D_range[1],N)
    x = np.array(x)
    y = lambda x: x *m + b + eps*(2*(R)-1)
    y = np.array(y(x))
    z = lambda a: (x + a * y)/(a**2 +1)
    F_a = lambda a: sum((x-z(a))**2 + (y - a* z(a))**2)
    a, ok = newton_raphson(F_a, X0)
    print("The optimized value of a is = ", a)
    print("The value of objective function F(a) = ", F_a(a))
    plt.scatter(x, y, color='green',marker = 'o')
    plt.plot(x, a*x, color = 'red', Linewidth = 2)
    plt.xlim(D_range[0], D_range[1])
    plt.ylim(D_range[0], D_range[1])
    plt.show()


total_least_squares()

    

