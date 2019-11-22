import numpy as np
import matplotlib.pyplot as plt

def univariatescan(f, X0, Alpha = 1e-2, tol = 1e-8, maxiter = 1e3):
    h = tol
    Fp = (f(X0+h) - f(X0))/(h)
    Fpp = (f(X0+h) - 2*f(X0) + f(X0-h))/(h**2)
    # Checking to see if the initial guess is a maximum
    if abs(Fpp) <= tol:
        print("Initial guess is a maximum or point of inflection")
        Xr = X0 + Alpha
        Xl = X0 - Alpha
        Fpp_Xr = (f(Xr+h) - 2*f(Xr) + f(Xr-h))/(h**2)
        Fpp_Xl = (f(Xl+h) - 2*f(Xl) + f(Xl-h))/(h**2)
        if Fpp_Xr > Fpp_Xl:
            X0 = Xr
        else:
            X0 = Xl
    if Fp == tol and Fpp > 0:
        print("The initial guess is the minimum")
        a = X0 + 2*Alpha
        b = X0 - 2*Alpha 
    if Fp > 0:
        delt = -Alpha
    else:
        delt = Alpha      
    Xk = X0
    Xk_f = Xk + delt
    F_Xk_f = f(Xk_f)
    F_Xk = f(Xk)
    k = 0
    while (F_Xk > F_Xk_f) and k < maxiter:
        delt = 2*delt
        Xk_b = Xk
        Xk = Xk_f
        Xk_f = Xk + delt
        F_Xk_f = f(Xk_f)
        F_Xk = f(Xk)
        a = min(Xk_b, Xk_f)
        b = max(Xk_b, Xk_f)
        k+=1
#    m = np.linspace(a-2, b+2, 100)
#    plt.plot(m, f(m), color = "red", linewidth = 2)
#    plt.plot([a,b], [f(a),f(b)], color = "blue", linestyle = '--')
#    plt.scatter(a, f(a), color = "green", marker = '*')
#    plt.scatter(b, f(b), color = "green", marker = '*')
#    plt.legend(("Obj. Func", "Bracketed Interval"), loc = "upper right")
#    plt.title("Scanned Interval")
#    plt.xlabel("x")
#    plt.ylabel("f(x)")
#    plt.show()
    return [a, b, k]

#f = lambda x : x**3 - 3* x**2
#x0 = 0.1
#
#A, B, k = univariatescan(f, x0)
#print("a =", A, "b = ", B, "No. of iterations = ", k)