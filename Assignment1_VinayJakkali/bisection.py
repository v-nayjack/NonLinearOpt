import numpy as np
import matplotlib.pyplot as plt


def bisection(f, a, b, tol=1e-8, maxiter=1e3):
    """ The bisection function defined here takes following parameters as input
    INPUT:
    f : it is defined as an lambda function
    a : lower bracketed interval point
    b : upper bracketed interval point. a and b can be obtained from univariatescan function
    tol : This is the tolerance accepted for the minimized objective function
    maxiter : Maximum iterations to stop the optimization

    OUTPUT:
    Plots showing objective function with the minimum point
    Also prints the values of total number of iterations, minimum x, minimum F(x) to the console

    Returns values of minimum(c) and total number of iterations (k)"""
    h = tol
    m = np.linspace(-10, 10, 100000)
    fp_a = (f(a + h) - f(a)) / h
    fpp_a = (f(a + h) - 2 * f(a) + f(a - h)) / (h ** 2)
    fp_b = (f(b + h) - f(b)) / h
    fpp_b = (f(b + h) - 2 * f(b) + f(b - h)) / (h ** 2)
    # Checking to see if the initial guess contains the minimum
    if abs(fp_a) == 0 and abs(fpp_a) > 0:
        print("The minimum is at point a")
        k = 1
        return a, k

    if abs(fp_b) == 0 and abs(fpp_b) > 0:
        print("The minimum is at point b")
        k = 1
        return b, k
    # Checking to see if one of the guesses is a maximum or point of inflection
    if abs(fpp_a) <= tol:
        print("Guess point 'a' is either the point of inflection or a maximum point")
        xr = a + 0.5
        xl = a - 0.5
        fpp_xr = (f(xr + h) - 2 * f(xr) + f(xr - h)) / (h ** 2)
        fpp_xl = (f(xl + h) - 2 * f(xl) + f(xl - h)) / (h ** 2)
        if fpp_xr > fpp_xl:
            a = xr
        else:
            a = xl
    if abs(fpp_b) <= tol:
        print("Guess point 'b' is either the point of inflection or a maximum point")
        xr = b + 0.5
        xl = b - 0.5
        fpp_xr = (f(xr + h) - 2 * f(xr) + f(xr - h)) / (h ** 2)
        fpp_xl = (f(xl + h) - 2 * f(xl) + f(xl - h)) / (h ** 2)
        if fpp_xr > fpp_xl:
            b = xr
        else:
            b = xl
    k = 0
    fv = []
    for i in range(len(m)):
        fv.append(f(m[i]))
    while (np.abs(a - b) >= tol) and k < maxiter:
        c = (a + b) / 2.0
        left = (a + c) / 2.0
        right = (c + b) / 2.0
        fl = f(left)
        fr = f(right)
        if fr > fl:
            b = right
        elif fl > fr:
            a = left
        else:
            a = left
            b = right
        k += 1
    print("Total no. of iterations to find the minimum of the Obj func = ", k)
    print("The minimum point is = ", round(c, 4))
    print("The minimum F(x) = ", round(f(c), 4))
    plt.plot(m, fv, color="red", linewidth=2)
    plt.scatter(c, f(c), color="b", marker='o')
    plt.title("F(x) minimization using bisection method", fontsize=24)
    plt.legend(("F(x)", "Minimum"), fontsize=20)
    plt.xlabel("x", fontsize=24)
    plt.ylabel("F(x)", fontsize=24)
    # plt.ylim(-12, 8)
    plt.xlim(-10, 10)
    plt.grid()
    # plt.axes().set_aspect('equal')
    plt.axes().axhline(y=0, color='k')
    plt.axes().axvline(x=0, color='k')
    plt.show()

    return c, k

# func = lambda x: x**2 + 2*x - 10
# a = 0.9
# b = 3.0
# tol = 1e-6
# maxiter = 1e3
# c, k=bisection(func,a,b,tol, maxiter)
#
# print(c, k)