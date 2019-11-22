import numpy as np
import matplotlib.pyplot as plt

def bisection(f, a, b, tol = 1e-8, maxiter = 1e3, D_range = (-5, 5)):

    h = tol
    m = np.linspace(-10, 10, 100000)
    Fp_a = (f(a+h) - f(a-h))/(2*h)
    Fpp_a = (f(a+h)-2*f(a) +f(a-h))/(h**2)
    Fp_b = (f(b+h) - f(b-h))/(2*h)
    Fpp_b = (f(b+h)-2*f(b) +f(b-h))/(h**2)
    # Checking to see if the initial guess contains the minimum
    if Fp_a == 0 and Fpp_a > 0:
        print("The minimum is at point a")
        iterations = 1
        return a, iterations
    
    if Fp_b == 0 and Fpp_b > 0:
        print("The minimum is at point b")
        iterations = 1
        return b, iterations
    # Checking to see if one of the guesses is a maximum or point of inflection
    if Fpp_a <= tol:
        print("Guess point 'a' is either the point of inflection or a maximum point")
        Xr = a + 0.5
        Xl = a - 0.5
        Fpp_Xr = (f(Xr+h) - 2*f(Xr) + f(Xr-h))/(h**2)
        Fpp_Xl = (f(Xl+h) - 2*f(Xl) + f(Xl-h))/(h**2)
        if Fpp_Xr > Fpp_Xl:
            a = Xr
        else:
            a = Xl
    if Fpp_b <= tol:
        print("Guess point 'b' is either the point of inflection or a maximum point")
        Xr = b + 0.5
        Xl = b - 0.5
        Fpp_Xr = (f(Xr+h) - 2*f(Xr) + f(Xr-h))/(h**2)
        Fpp_Xl = (f(Xl+h) - 2*f(Xl) + f(Xl-h))/(h**2)
        if Fpp_Xr > Fpp_Xl:
            b = Xr
        else:
            b = Xl
    iterations = 0
    F = []
    for i in range(len(m)):
        F.append(f(m[i]))
    while (np.abs(a-b)>= tol) and iterations < maxiter:
        c = (a+b)/2.0
        L = (a+c)/2.0
        R = (c+b)/2.0
        FL = f(L)
        FR = f(R)
        if FR > FL:
            b = R
        elif FL > FR:
            a = L
        else:
            a = L
            b = R
        iterations += 1
        
    
    plt.plot(m, F, color = "red", linewidth = 2)
    plt.scatter(c,f(c), color = "blue", marker = 'o')
    plt.title("Objective Function")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()
    
    return c, iterations

#func = lambda x: x**3 - 3* x**2
#a = 0.9
#b = 3.0
#tol = 1e-6
#maxiter = 1e3
#c, iterations=bisection(func,a,b,tol, maxiter)
#
#print(c, iterations)

