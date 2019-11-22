import numpy as np

def newton_raphson(f, X0, tol = 1e-8, Alpha = 1e-2, maxiter = 1e3):
    if Alpha < 0:
        Alpha = abs(Alpha)
    h = Alpha
    iterations = 0
    
    while iterations < maxiter:
        Fp = (f(X0+h) - f(X0-h))/(2*h)
        Fpp = (f(X0+h)-2*f(X0) +f(X0-h))/(h**2)
                # Checking to see if the initial guess is a maximum
        if Fpp <= 0:
            print("Initial guess is a maximum or point of inflection")
            Xr = X0+1.0
            Xl = X0-1.0
            Fpp_Xr = (f(Xr+h) - 2*f(Xr) + f(Xr-h))/(h**2)
            Fpp_Xl = (f(Xl+h) - 2*f(Xl) + f(Xl-h))/(h**2)
            if Fpp_Xr > Fpp_Xl:
                X0 = Xr
            else:
                X0 = Xl
        # Condition for local minimum
        if Fp == tol and Fpp > tol:
            print ("Initial guess entered is the minimum")
            break
        Xn = X0 - (Fp/Fpp)
        if np.abs(f(Xn)-f(X0)) <= tol:
            break
        X0 = Xn
        iterations+=1
#        print(Xn, iterations)
    return Xn, iterations


f = lambda x: x**3 - 3* x**2

x0 = 0.5

minimum, no_of_iterations = newton_raphson(f,x0)

if no_of_iterations > 0:
    print("minimum =",minimum, "No. of iterations = ", no_of_iterations)
else:
    print("Solution not found. Try again!")