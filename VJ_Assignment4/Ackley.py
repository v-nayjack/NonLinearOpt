# Created by Vinay Jakkali on 12/12/2019

"""
--------------------------------------------------------------------------------------
The rosenbrock function defined here takes following parameters as input

INPUT:
    x : It is vector of 2 variables in 'x'

OUTPUT:
    1. Ackley function of 2 variables

--------------------------------------------------------------------------------------
"""

import numpy as np
import math


def ackley(x):

    A = -0.2 * (0.5 * (x[0])**2 + x[1]**2)**0.5

    B = 0.5 * sum(np.cos(2 * np.pi * x))

    Obj_Func = -20. * np.exp(A) - np.exp(B) + np.exp(1) + 20

    return Obj_Func

