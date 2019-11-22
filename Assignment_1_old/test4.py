import numpy as np
#import random

#from Newton import newton_raphson
from Univariatescan_new import univariatescan
from Bisection_new import bisection
#import matplotlib.pyplot as plt


P = (5.0,3.0)
c = (2.0,2.0)
r = 1.0
rho = 20
X0 = 0.5
tol = 1e-8


A = lambda x : (x - P[0])**2 + (P[1])**2
B = lambda x : 2*((P[0] - x)*(x - c[0]) - (P[1]*c[1]))
C = lambda x : (x - c[0])**2 + (c[1])**2 - r**2
delta = lambda x : B(x)**2 - 4*A(x)*C(x)



F = lambda x: (x + ((A(x))**(0.5)) * (1 + rho * abs((((delta(x))**(0.5))/(A(x))))))  if delta(x)>0 else x + ((A(x))**(0.5)) 
#l = np.array([1,2])
#print(l)
#print(A(l))
#print(B(l))
#print(C(l))
#print(delta(l))
#print(F(2))
[a, b, k] = univariatescan(F, X0)
print(a,b)
X, ok = bisection(F, a, b)
print(X)
#Y, Ok = newton_raphson(F, X0)
print(F(X))
#print(F(Y))