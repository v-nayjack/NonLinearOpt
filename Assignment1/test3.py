# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 14:07:20 2018

@author: Vinay
"""
import numpy as np
import random
N = 10
D_range = (-5,5)
m = 0.5
b = 0.0
eps = 1e-2
R = random.random()
x = np.linspace(D_range[0],D_range[1],N)
Y = lambda x: x *m + b + eps*(2*(R)-1)
y = np.array(Y(x))
Data = np.column_stack((x,y))
Z = []
Fa = lambda a: []
Obj = lambda a: 0

z = lambda a : (x + a * y)/(a**2 +1)

    
Obj = lambda a: sum((x-z(a))**2 + (y - a* z(a))**2)

#z = []
#z[1,:] = lambda a: x[1,:] - a* y[1,:]/(a**2 +1)
#for i in range(N):
#    z[i] = lambda a: x[i] - a* y[i]/(a**2 +1)

#zi = lambda a: (Data[:,0] + a*Data[:,1])/(a**2 +1)
#f_a = sum((x - zi)**2 + (y - zi)**2)
#def Data(N = 100, D_range  = (-5,5), m = 0.5, b = 0, eps = 1e-2):
#    R = random.random()
#    x = np.linspace(D_range[0],D_range[1],N)
#    f = lambda x: x *m + b + eps*(2*(R)-1)
#    y = np.array(f(x))
#    data = np.column_stack((x,y))
#    return data

