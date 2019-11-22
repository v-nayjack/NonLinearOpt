'''
Created on Sep 22, 2018

@author: vinay
'''


import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


x = sp.symbols('x')

func = x**3-3*x**2
a = 1.0
b = 6.0
tol = 1e-6
c=0.0
while (np.abs(a-b)>=tol):
    c = (a+b)/2.0
    L = (a+c)/2.0
    R = (c+b)/2.0
    Fa = func.subs(x,a)
    Fb = func.subs(x,b)
    Fc = func.subs(x,c)
    FL = func.subs(x,L)
    FR = func.subs(x,R)
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
print(c)

sp.plot(func, (x, -1,4),line_color = 'r')


x, y = sp.symbols("x y")
hp = sp.plot_implicit(sp.Eq(x**2 + y**2, 4), (x, -3, 3), (y, -3, 3))
fig = hp._backend.fig
ax = hp._backend.ax
xx = yy = np.linspace(-3,3)
ax.plot(xx,yy) # y = x
ax.plot([0],[0],'o') # Point (0,0)
ax.set_aspect('equal','datalim')
fig.canvas.draw()