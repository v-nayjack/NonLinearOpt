import sympy as sp

def secant(func,X0, X1, tol= 1e-6, maxiter = 1e2):
    x = sp.symbols('x')
    Fp = sp.diff(func, x)
    Xn_f = 0.0
    Xn = X1
    Xn_b = X0
    Fp_Xn = Fp.subs(x, Xn)
    iterations = 0

    while abs(Fp_Xn) > tol and iterations < maxiter:
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
'''
x = sp.symbols('x')
f = x**3-3*x**2

x0 = 1
x1 = 2.1

minimum, no_of_iterations = secant(f,x0,x1)

if no_of_iterations > 0:
    print("minimum =",minimum, "No. of iterations = ", no_of_iterations)
else:
    print("Solution not found. Try again!")'''

