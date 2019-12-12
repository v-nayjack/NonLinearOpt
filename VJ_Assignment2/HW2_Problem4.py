# Created by Vinay Jakkali on 12/9/2019

"""
--------------------------------------------------------------------------------------
Problem 4 calculations to minimize the give two dimensional function using Powell's
Method or Quasi-Newton Method
--------------------------------------------------------------------------------------
"""
import numpy as np
from Quasi_Newton import quasi_newton, quasi_newton_surfaceplot, quasi_newton_contourplot


def f(x):

    F = (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

    return F


def main():

    Fmins = lambda x: f(x)

    Fmaxs = lambda x: -1 * f(x)

    X0 = np.array([[-5., -2.], [5., -2.5], [-3., 3.8], [4.75, 1.8], [3., 2.]])

    Minimums = np.zeros(np.shape(X0))

    Maximums = np.zeros(np.shape(X0))

    F_mins = np.zeros(len(X0))

    F_maxs = np.zeros(len(X0))

    for i in range(len(X0)):

        Minimums[i, :], k1 = quasi_newton(Fmins, X0[i, :])

        F_mins[i] = Fmins(Minimums[i, :])

        Maximums[i, :], k2 = quasi_newton(Fmaxs, X0[i, :])

        F_maxs[i] = Fmaxs(Maximums[i, :])

    return np.around(Minimums, decimals=2), np.around(Maximums, decimals=2), F_mins, F_maxs



if __name__ == '__main__':

    Mins, Maxs, f_mins, f_maxs = main()


    TotalMins = np.unique(f_mins)

    TotalMaxs = np.where(np.unique(f_maxs >= 0.))[0]

    quasi_newton_contourplot(f, Mins[0, :])
    quasi_newton_surfaceplot(f, Mins[0, :])


    print("Minimums", Mins)
    print("Maximums", Maxs)

    print("Total no. of minimums", len(TotalMins))
    print("Total no. of maximums", len(TotalMaxs))




