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
from Quasi_Newton import quasi_newton, quasi_newton_contourplot, quasi_newton_surfaceplot
from PowellMethod import powell_method, powell_contourplot, powell_surfaceplot

def rosenbrock(x):

    N = len(x)
    F = 0.0


    for i in range(N-1):

        F = F + (100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2)

    return F

if __name__ == "__main__":

    X0 = np.array([2.55, 1.75])

    L = np.array([-2., -2.])

    U = np.array([2., 2.])

    QN_minX, QN_K = quasi_newton(rosenbrock, X0)

    print("Quasi Newton Minimum  ", QN_minX)
    print('Quasi Newton Fmin', rosenbrock(QN_minX))
    print("Quasi Newton total no. of iterations = ", QN_K)

#    P_minX, P_K = powell_method(rosenbrock, X0, L, U)


#    print("Powell Method Minimum  ", P_minX)
#    print('Powell Method Fmin', rosenbrock(P_minX))
#    print("Powell Method total no. of iterations = ", P_K)

    # Plotting the Rosenbrock function
    quasi_newton_surfaceplot(rosenbrock, QN_minX)
    quasi_newton_contourplot(rosenbrock, QN_minX)
