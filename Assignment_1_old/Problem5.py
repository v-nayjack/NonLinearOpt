import numpy as np
from Newton import newton_raphson

def routing(P = (5,5), c = (2.5,2.5), r = 2.0, rho = 0.05, X0 = 2.5, tol = 1e-8):
    A = lambda x : (x - P[0])**2 + (P[1])**2
    B = lambda x : 2*((P[0] - x)*(x - c[0]) - (P[1]*c[1]))
    C = lambda x : (x - c[0])**2 + (c[1])**2 + r**2
    delta = lambda x : B(x)**2 - 4*A(x)*C(x)
    
#    if delta <= tol:
#        F = lambda x: (x + A(x)**0.5)
#    else:
#        F = lambda x: (x + A(x)**0.5 * (1 + rho* abs((delta(x)**0.5)/(A(x))))
    F = lambda x: (x + A(x)**0.5 * (1 + rho* abs((delta(x)**0.5)/(A(x)))))    
    x, ok = newton_raphson(F, X0)
    

