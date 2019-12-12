# Created by Vinay Jakkali on 12/12/2019

"""
--------------------------------------------------------------------------------------
Include code description here:

--------------------------------------------------------------------------------------
"""

import numpy as np
import math


def ackley(x):

    A = -0.2 * (0.5 * (x[0])**2 + x[1]**2)**0.5

    B = 0.5 * sum(np.cos(2 * np.pi * x))

    Obj_Func = -20. * math.exp(A) - math.exp(B) + math.exp(1) + 20

    return Obj_Func

