# Created by Vinay Jakkali on 12/11/2019

"""
--------------------------------------------------------------------------------------
Include code description here:

--------------------------------------------------------------------------------------
"""

import numpy as np
from scipy.optimize import minimize

def al_inequality(F, c, x0, r0=0.25, v0=1, beta=0.1, maxiter=1e3):

    k = 0

    while k < maxiter:

        """ Augmented Lagrangian Function with Inequality Constraints """
        C = c(x0) - (r0/2)*v0

        C = C[C < 0]


        F_al_ineq = lambda x: F(x) + (1/r0) * sum(C**2)

        """ Unconstrained Optimization """

        res = minimize(F_al_ineq, x0, method='Powell', options={'xtol': 1e-8, 'disp': False})
        xk = res.x


        """ Updating v for Inequality Constraints """

        if c(xk) < (r0/2) * v0:

            vk = v0 - ((2/r0) * c(xk))
        else:

            vk = 0


        """ Updating r """

        rk = beta * r0

        """ Updating all values for next iteration """

        r0 = rk
        v0 = vk
        delta_x = x0 - xk
        x0 = xk

        """ Iteration number update """
        k += 1

        """ Stopping Criteria """

        if np.linalg.norm(c(x0)) <= 1e-8:
            return x0

        if abs(np.linalg.norm(delta_x)) <= 1e-5:
            return x0

    return x0
