import sympy as sp

from UnivariateScanMethod import univariatescan
x = sp.symbols('x')
f = x**3-3*x**2
a,b = univariatescan(f, 1, 0.01)
print(a,b)



