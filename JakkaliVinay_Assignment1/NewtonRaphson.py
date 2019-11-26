# Created by Vinay Jakkali on 11/25/2019

"""
--------------------------------------------------------------------------------------
The newton_raphson function defined here takes following parameters as input

INPUT:
f : It is defined as an anonymous function

x0 : It is initial guess required for Newton Raphson method

tol : This is the tolerance accepted for the minimized objective function
(by default tol = 1e-8)

alp : This is the step size
(by default alp = 1e-2)

maxiter : Maximum iterations to stop the optimization
(by default maxiter = 1e3)

OUTPUT:
1. Returns the values of minimum 'xn' and total number of iterations 'k'

2. A new window with the plot showing objective function with the minimum point

3. Print the values of total number of iterations 'k', minimum 'x', minimum 'F(x)' to the console
--------------------------------------------------------------------------------------
"""

import numpy as np
import matplotlib.pyplot as plt


def newton_raphson(f, x0, tol=1e-8, alp=1e-2, maxiter=1e3):

    if alp < 0:
        alp = abs(alp)

    k = 0
    xn = 0.0

    """ The stopping criteria used --> Checking condition maximum iterations {k < maxiter}"""

    while k < maxiter:

        fp = (f(x0+alp) - f(x0))/alp
        fpp = (f(x0+alp)-2*f(x0) + f(x0-alp))/(alp**2)

        # Checking to see if the initial guess is a maximum
        if fpp <= 0:

            print("Initial guess is a maximum or point of inflection")

            xr = x0+1.0
            xl = x0-1.0

            fpp_xr = (f(xr+alp) - 2*f(xr) + f(xr-alp))/(alp**2)
            fpp_xl = (f(xl+alp) - 2*f(xl) + f(xl-alp))/(alp**2)

            if fpp_xr > fpp_xl:
                x0 = xr

            else:
                x0 = xl

        # Condition for local minimum

        if fp == tol and fpp > tol:

            print("Initial guess entered is the minimum")
            break

        xn = x0 - (fp/fpp)

        if np.abs(f(xn)-f(x0)) <= tol:
            break

        x0 = xn
        k += 1

    return round(xn, 4), k


""" Function 'myplot' plots the objective function along with the minimum """

def myplot(xn, f):

    """ Creating points for plotting the objective function """

    m = np.linspace(-10, 10, 1000)
    fv = []

    for i in range(len(m)):
        fv.append(f(m[i]))

    plt.figure()
    plt.plot(m, fv, color="red", linewidth=2)
    plt.scatter(xn, f(xn), color="blue", marker='o')
    plt.title("Objective function", fontsize=20)
    plt.legend(("F(x)", "Minimum"), fontsize=14)
    plt.xlabel("x", fontsize=16)
    plt.ylabel("F(x)", fontsize=16)
    plt.grid()
    plt.axes().axhline(y=0, color='k')
    plt.axes().axvline(x=0, color='k')

    return plt.show()

if __name__ == "__main__":

    Func = lambda x: x**3 - 3*x**2

    X0 = 2.5

    Xn, K = newton_raphson(Func, X0)
    myplot(Xn, Func)

    print(" Total no. of iterations to find the minimum of the Obj func = ", K)
    print(" The minimum point is = ", Xn)
    print(" The minimum F(x) = ", round(Func(Xn), 2))
