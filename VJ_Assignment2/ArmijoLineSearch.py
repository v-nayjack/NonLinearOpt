# Created by Vinay Jakkali on 12/8/2019

"""
--------------------------------------------------------------------------------------
The armijolinesearch function defined here takes following parameters as input

INPUT:
    F : It is the objective function

    x0 : It is an array of size Nx1 initial guesses required for Quasi Newton method

    pk : It is an array of size Nx1 containing search directions

    maxiter : Maximum iterations to stop the optimization
    (by default maxiter = 1e3)

OUTPUT:
    1. Returns the values of minimum 'X_k' and total number of iterations 'k'

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
    S = 1.
    k=0
    g = gradient(F, X0)

    v = np.dot(np.transpose(Pk), g).flatten()


    if v[0] == 0.:
        D = v
        return S

    D = lambda s: (F(X0 + s * Pk.flatten()) - F(X0)) / (s * v)


    while k < maxiter:


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


