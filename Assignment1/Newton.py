import numpy as np
import matplotlib.pyplot as plt


def newton_raphson(f, x0, tol=1e-8, alp=1e-2, maxiter=1e3):
    """ The newton_raphson function defined here takes following parameters as input
    INPUT:
    f : it is defined as an lambda function
    x0 : it is initial guess required for Newton Raphson method
    tol : This is the tolerance accepted for the minimized objective function
    alp : This is the step size
    maxiter : Maximum iterations to stop the optimization

    OUTPUT:
    Plots showing objective function with the minimum point
    Also prints the values of total number of iterations, minimum x, minimum F(x) to the console

    Returns values of minimum(xn) and total number of iterations (k)"""
    if alp < 0:
        alp = abs(alp)
    h = alp
    k = 0
    m = np.linspace(-10, 10, 100000)
    fv = []
    for i in range(len(m)):
        fv.append(f(m[i]))
    while k < maxiter:
        fp = (f(x0+h) - f(x0))/h
        fpp = (f(x0+h)-2*f(x0) + f(x0-h))/(h**2)
        # Checking to see if the initial guess is a maximum
        if fpp <= 0:
            print("Initial guess is a maximum or point of inflection")
            xr = x0+1.0
            xl = x0-1.0
            fpp_xr = (f(xr+h) - 2*f(xr) + f(xr-h))/(h**2)
            fpp_xl = (f(xl+h) - 2*f(xl) + f(xl-h))/(h**2)
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
    print("Total no. of iterations to find the minimum of the Obj func = ", k)
    print("The minimum point is = ", round(xn, 4))
    print("The minimum F(x) = ", round(f(xn), 4))
    plt.plot(m, fv, color="red", linewidth=2)
    plt.scatter(xn, f(xn), color="blue", marker='o')
    plt.title("Objective function", fontsize=24)
    plt.legend(("F(x)", "Minimum"), fontsize=20)
    plt.xlabel("x", fontsize=24)
    plt.ylabel("F(x)", fontsize=24)
    # plt.ylim(0, 30)
    # plt.xlim(-2, 8)
    plt.grid()
    # plt.axes().set_aspect('equal')
    plt.axes().axhline(y=0, color='k')
    plt.axes().axvline(x=0, color='k')
    plt.show()
    return xn, k


# f = lambda x: x**2 - 6*x + 10
#
# x0 = 2.5
#
# minimum, no_of_k = newton_raphson(f,x0)
#
# if no_of_k > 0:
#     print("minimum =",minimum, "No. of k = ", no_of_k)
# else:
#     print("Solution not found. Try again!")