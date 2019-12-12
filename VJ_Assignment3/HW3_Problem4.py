# Created by Vinay Jakkali on 12/11/2019

"""
--------------------------------------------------------------------------------------
Problem 4 calculations to minimize Rosenbrock Function for all the given constraints
--------------------------------------------------------------------------------------
"""

import numpy as np
from scipy.optimize import minimize
from Rosenbrock import rosenbrock
from AugmentedLagrangian import augmentedlagrangian as AL
from AugmentedLagrangian_Equality import al_equality
from AugmentedLagrangian_Inequality import al_inequality

def main():

    """ Calculating local minimum for Rosenbrock function for all given constraints"""


    """ Calling the Rosenbrock function """

    Obj_Func = lambda x: rosenbrock(x)


    """ Initial Guess X0 of size N """

    X0 = np.array([0.5, 0.5])


    """ Getting the dimensions of the initial guess array X0 """

    N = len(X0)


    """ Problem 4a Constraints and minimum calculation """

    c_4a = lambda x: np.linalg.norm(x) ** 2 - 1  # given constraint

    Xk_4a = al_equality(Obj_Func, c_4a, X0)


    """ Problem 4b Constraints and minimum calculation """

    C = np.array([-1])  # creating an array C = [-1, 1, 1, ...., 1]

    C = np.concatenate([C, np.ones(N - 1)])  # creating an array C = [-1, 1, 1, ...., 1]

    c_4b = lambda x: np.linalg.norm(x - C) ** 2 - 1

    Xk_4b = al_equality(Obj_Func, c_4b, X0)


    """ Problem 4c Constraints and minimum calculation """

    c_4c = lambda x: 1 - np.linalg.norm(x) ** 2

    Xk_4c = al_inequality(Obj_Func, c_4c, X0)


    """ Problem 4d Constraints and minimum calculation """

    c_4d = lambda x: 1 - np.linalg.norm(x - C) ** 2

    Xk_4d = al_inequality(Obj_Func, c_4d, X0)


    """ Problem 4e Constraints and minimum calculation """

    C = 0.5 * C

    c_eq_4e = lambda x: np.linalg.norm(x - C) ** 2 - 1

    c_ineq_4e = lambda x: 1 - np.linalg.norm(x) ** 2

    Xk_4e = AL(Obj_Func, c_eq_4e, c_ineq_4e, X0)


    """Returning the minimums calculated for all the given constraints"""

    return Xk_4a, Xk_4b, Xk_4c, Xk_4d, Xk_4e


if __name__ == '__main__':

    Min_4a, Min_4b, Min_4c, Min_4d, Min_4e = main()

    print("Problem 4a Minimum ", Min_4a)
    print("Problem 4b Minimum ", Min_4b)
    print("Problem 4c Minimum ", Min_4c)
    print("Problem 4d Minimum ", Min_4d)
    print("Problem 4e Minimum ", Min_4e)
