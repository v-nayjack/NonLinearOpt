import sympy as sp

def secant(func,X0, X1, tol= 1e-6, maxiter = 1e2):
    Fp = sp.diff(func, x)
    Fpp = sp.diff(func, x, x)
    Xn_f = 0.0
    Xn = X1
    Xn_b = X0
    Fp_Xn = Fp.subs(x, Xn)
    iterations = 0
    if Fpp.subs(x, X0) <= tol:
        X0right = X0 + 0.01
        X0left = X0 - 0.01
        if Fp.subs(x,X0right) > Fp.subs(x, X0left):
            X0 = X0right
        else:
            X0 = X0left
            
    if Fpp.subs(x, X1) <= tol:
        X1right = X1 + 0.01
        X1left = X1 - 0.01
        if Fp.subs(x, X1right) > Fp.subs(x, X1left):
            X1 = X1right
        else:
            X1 = X1left
            
    while abs(Fp_Xn) > tol and iterations < maxiter:
        if Fp.subs(x, X0) == tol and Fpp.subs(x, X0) > tol:
            Xn_f = X0
            break
        if Fp.subs(x, X1) == tol and Fpp.subs(x, X1) > tol:
            Xn_f = X1
            break
        Fp_Xn = Fp.subs(x, Xn)
        Fp_Xnb = Fp.subs(x, Xn_b)
        Xn_f = Xn - ((Xn - Xn_b)* Fp_Xn)/(Fp_Xn - Fp_Xnb)
        Fp_Xnf = Fp.subs(x, Xn_f)
        if Fp_Xnf == tol:
            break
        
        if Fp_Xnf > tol:
            Xn = Xn_f
        elif Fp_Xnf < tol:
            Xn_b = Xn_f
        iterations += 1

    return Xn_f, iterations

x = sp.symbols('x')
f = x**3-3*x**2

x0 = 0.0
x1 = 6.0

minimum, no_of_iterations = secant(f,x0,x1)

if no_of_iterations > 0:
    print("minimum =",minimum, "No. of iterations = ", no_of_iterations)
else:
    print("Solution not found. Try again!")
