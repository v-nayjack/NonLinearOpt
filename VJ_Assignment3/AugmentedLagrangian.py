# Created by Vinay Jakkali on 12/11/2019

"""
--------------------------------------------------------------------------------------
Include code description here:

--------------------------------------------------------------------------------------
"""
import numpy as np
from scipy.optimize import minimize
from autograd import jacobian, hessian

def augmentedlagrangian(F, c_eq, c_ineq, x0, r0=0.25, v0_eq=1, v0_ineq=1, beta=0.1, maxiter=1e3):

    k = 0

    while k < maxiter:

        """ Augmented Lagrangian Function with both Equality and Inequality Constraints """

        C_ineq = c_ineq(x0) - (r0/2)*v0_ineq

        C_ineq = C_ineq[C_ineq < 0]


        F_al_both = lambda x: F(x) + (1/r0) * (np.linalg.norm(c_eq(x) - ((r0/2) * v0_eq)))**2 \
                                  + (1/r0) * sum(C_ineq**2)

        """ Unconstrained Optimization """

        res = minimize(F_al_both, x0, method='Powell', options={'xtol': 1e-8, 'disp': False})
        xk = res.x


        """ Updating v for Equality Constraints """

        vk_eq = v0_eq - ((2/r0) * c_eq(xk))

        """ Updating v for Inequality constraints """

        if c_ineq(xk) < (r0/2) * v0_ineq:

            vk_ineq = v0_ineq - ((2/r0) * c_ineq(xk))

        else:

            vk_ineq = 0


        """ Updating r """

        rk = beta * r0

        """ Updating all values for next iteration """

        r0 = rk
        v0_eq = vk_eq
        v0_ineq = vk_ineq
        delta_x = x0 - xk
        x0 = xk

        """ Iteration number update """
        k += 1

        """ Stopping Criteria """

        if np.linalg.norm(c_eq(x0)) <= 1e-8 and np.linalg.norm(c_ineq(x0)) <= 1e-8:
            return x0

        if abs(np.linalg.norm(delta_x)) <= 1e-5:
            return x0

    return x0

