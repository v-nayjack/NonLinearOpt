
import sympy as sp



x = sp.symbols('x')

func = x**3-3*x**2
x0 = 1.0
x1 = 6.0
tol = 1e-6
iteration = 0
Fp = sp.diff(func,x)
fx0 = Fp.subs(x, x0)
fx1 = Fp.subs(x, x1)
xn_f = 0.0
xn_b = x0
xn = x1
Fp_xn = Fp.subs(x,xn)
while abs(Fp_xn) > tol and iteration <100:
    Fp_xn = Fp.subs(x,xn)
    Fp_xnb = Fp.subs(x,xn_b)
    xn_f = xn - ((xn-xn_b)*Fp_xn)/(Fp_xn - Fp_xnb)
    Fp_xnf = Fp.subs(x, xn_f)
    if Fp_xnf >= tol:
        break
    
    if Fp_xnf > 0:
        xn = xn_f
    elif Fp_xnf <0:
        xn_b = xn_f
    iteration += 1    
    
   
print(xn_f,iteration)   
