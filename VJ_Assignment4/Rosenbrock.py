# Created by Vinay Jakkali on 12/8/2019

"""
--------------------------------------------------------------------------------------
The rosenbrock function defined here takes following parameters as input

INPUT:
    x : It is vector of N variables in 'x'

OUTPUT:
    1. Rosenbrock function of N variables
--------------------------------------------------------------------------------------
"""

import numpy as np

def rosenbrock(x):

    N = len(x)

    F = 0.0

    for i in range(N-1):

        F = F + (100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2)

    return F
