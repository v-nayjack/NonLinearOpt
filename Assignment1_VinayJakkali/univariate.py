import numpy as np
import matplotlib.pyplot as plt


def univariatescan(f, x0, tol=1e-8, alp=1e-2, maxiter=1e3):
    """ The univariatescan function defined here takes following parameters as input
    INPUT:
    f : it is defined as an lambda function
    x0 : it is initial guess required for Newton Raphson method
    tol : This is the tolerance accepted for the minimized objective function
    alp : This is the step size
    maxiter : Maximum iterations to stop the optimization

    OUTPUT:
    Plots showing objective function with the bracketed interval
    Also prints the values of total number of iterations, a and b to the console

    Returns values of lower bracketed point(a), upper bracketed point(b) and total number of iterations (k)"""
    h = tol
    fp = (f(x0+h) - f(x0))/h
    fpp = (f(x0+h) - 2*f(x0) + f(x0-h))/(h**2)
    '''Checking to see if the initial guess is a maximum or point of inflection
    if the guess point is a maximum or point of inflection, the function takes small steps left and right
    of the guess point. After this, the condition checks for the appropriate direction to look for the interval '''
    if abs(fpp) <= tol:
        print("Initial guess is a maximum or point of inflection")
        xr = x0 + 1.0
        xl = x0 - 1.0
        fpp_xr = (f(xr+h) - 2*f(xr) + f(xr-h))/(h**2)
        fpp_xl = (f(xl+h) - 2*f(xl) + f(xl-h))/(h**2)
        if fpp_xr > fpp_xl:
            x0 = xr
        else:
            x0 = xl
    ''' Checking to see if the user guessed the minimum'''
    if fp == 0 and fpp > 0:
        print("The initial guess is the minimum")
        a = x0 + 2
        b = x0 - 2
        k = 0
        return [a, b, k]
    '''Actual calculation to find the bracket starts here.
     Determining the sign of the delta based on the first derivative of the obj. function'''
    if fp > 0:
        delta = -alp
    else:
        delta = alp
    xk = x0
    xk_f = xk + delta
    f_xk_f = round(f(xk_f), 4)
    f_xk = round(f(xk), 4)
    k = 0
    a = min(xk, xk_f)
    b = max(xk, xk_f)
    '''After calculating initial values, the function iterates to update the values of Xn and Xn_1
    The stopping criteria used is the condition F(Xn_1) > F(Xn) and maximum iterations'''
    while (f_xk > f_xk_f) and k < maxiter:
        delta = 2*delta
        xk_b = xk
        xk = xk_f
        xk_f = xk + delta
        f_xk_f = f(xk_f)
        f_xk = f(xk)
        a = min(xk_b, xk_f)
        b = max(xk_b, xk_f)
        '''The following conditions check whether a & b are negative and kicks them back to +ve side'''
        if a < 0 and b < 0:
            xk = 10*x0
        elif a < 0:
            xk = 10*x0
            delta = -1*delta
            f_xk = f(b)
            f_xk_f = f(a)
        k += 1
    print("The total number of iterations to find the bracket = ", k)
    print("The Bracket values are", round(a, 4), round(b, 4))
    m = np.linspace(-10, 10, 100000)
    fv = []
    for i in range(len(m)):
        fv.append(f(m[i]))
    plt.plot(m, fv, color="red", linewidth=2)
    plt.plot([a, b], [f(a), f(b)], color = "blue", linestyle='--')
    plt.scatter(a, f(a), color="green", marker='*')
    plt.scatter(b, f(b), color="green", marker='*')
    plt.legend(("F(x)", "Bracketed Interval"), fontsize=24)
    plt.title("Bracketed Interval", fontsize=24)
    # plt.xlim(-7, 7)
    plt.xlabel("x", fontsize=24)
    plt.ylabel("F(x)", fontsize=24)
    # plt.ylim(-12, 8)
    plt.grid()
    # plt.axes().set_aspect('equal')
    plt.axes().axhline(y=0, color='k')
    plt.axes().axvline(x=0, color='k')
    plt.show()

    plt.show()

    return [a, b, k]

# f = lambda x : x**2 + 2* x - 10
# x0 = 0.0
#
# A, B, k = univariatescan(f, x0)
# print("a =", A, "b = ", B, "No. of iterations = ", k)