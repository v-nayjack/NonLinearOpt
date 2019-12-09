# Created by Vinay Jakkali on 12/8/2019

"""
--------------------------------------------------------------------------------------
Include code description here:

--------------------------------------------------------------------------------------
"""

import numpy as np

from Gradient import gradient

def armijolinesearch(F, x0, pk, maxiter=1e3):

    X0 = np.copy(x0)
    Pk = np.copy(pk)

    C = 1.1
    c = 0.9
    eta1 = 0.4
    eta2 = 0.4
    S = 1
    k=0
    g = gradient(F, X0)

    while k < maxiter:

        D = lambda s: (F(X0 + s * Pk.flatten()) - F(X0))/(s * np.dot(np.transpose(Pk), g))

        if abs(1-D(S)) <= eta2:
            S_min = S
            S = C*S

        else:
            break

        S = S_min + c*(S-S_min)
        k += 1

        if D(S) <= eta1:
            break

    return S


