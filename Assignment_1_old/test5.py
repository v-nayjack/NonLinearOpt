# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 15:18:48 2018

@author: Vinay
"""

import numpy as np


def univariatescan(f, X0, Alpha = 1e-2, tol = 1e-8, maxiter = 1e3):
    h = Alpha
    Fp = (f(X0+h) - f(X0))/(h)
    Fpp = (f(X0+h)-2*f(X0) +f(X0-h))/(h**2)
    # Checking to see if the initial guess is a maximum
    if Fpp <= 0:
        print("Initial guess is a maximum or point of inflection")
        Xr = X0 + 1.0
        Xl = X0 - 1.0
        Fpp_Xr = (f(Xr+h) - 2*f(Xr) + f(Xr-h))/(h**2)
        Fpp_Xl = (f(Xl+h) - 2*f(Xl) + f(Xl-h))/(h**2)
        if Fpp_Xr > Fpp_Xl:
            X0 = Xr
        else:
            X0 = Xl
#    delt =(-(Alpha) * (np.sign(Fp)))
    if Fp > 0:
        delt = -Alpha
    else:
        delt = Alpha
        
    Xk = X0
    Xk_f = Xk + delt
    F_Xk_f = f(Xk_f)
    F_Xk = f(Xk)
    a = Xk
    b = Xk_f
    k = 0
    
    while ((F_Xk_f>F_Xk) == False) and k < maxiter:
        # Condition for local minimum
        Xk_f = Xk + delt
        a = min(Xk, Xk_f)
        b = max(Xk, Xk_f)
        delt = 2 * delt
        Xk = Xk_f        
        F_Xk_f = f(Xk_f)
        F_Xk = f(Xk)
        k+=1
    return [a, b, k]