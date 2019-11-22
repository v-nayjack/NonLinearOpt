

import sympy as sp
import numpy as np


def bisection(func,a,b,tol = 1e-8, maxiter = 1e2):
    y = sp.symbols('x')
    Fp = sp.diff(func, y)
    Fpp = sp.diff(func, y, y)
    iterations = 0
    if Fpp.subs(y, a) <= tol:
        aright = a + 0.01
        aleft = a - 0.01
        if Fp.subs(y,aright) > Fp.subs(y, aleft):
            a = aright
        else:
            a = aleft
            
    if Fpp.subs(y, b) <= tol:
        bright = b + 0.01
        bleft = b - 0.01
        if Fp.subs(y, bright) > Fp.subs(y, bleft):
            b = bright
        else:
            b = bleft
        
    
    while (np.abs(a-b)>=tol) and iterations < maxiter:
        if Fp.subs(y, a) == tol and Fpp.subs(y, a) > tol:
            c = a
            break
        if Fp.subs(y, b) == tol and Fpp.subs(y, b) > tol:
            c = b
            break
        
        c = (a+b)/2.0
        L = (a+c)/2.0
        R = (c+b)/2.0
        Fa = func.subs(y,a)
        Fb = func.subs(y,b)
        Fc = func.subs(y,c)
        FL = func.subs(y,L)
        FR = func.subs(y,R)
        Fmin = min(Fa,Fb,Fc,FL,FR)
        
        if Fmin == Fa or Fmin == FL:
            b = c
            c = L
        elif Fmin == Fb or Fmin == FR:
            a = c
            c = R            
        elif Fmin == Fc:
            a = L
            b = R
        iterations += 1    
    return c, iterations

x = sp.symbols('x')

func = x**3-3*x**2
a = 0.0
b = 2.0
tol = 1e-6
maxiter = 1e3
c, iterations=bisection(func,a,b,tol, maxiter)

print(c, iterations)

sp.plot(func, (x, -1,4),line_color = 'r')
           

