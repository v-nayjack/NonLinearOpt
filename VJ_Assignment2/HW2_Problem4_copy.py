# Created by Vinay Jakkali on 12/12/2019

"""
--------------------------------------------------------------------------------------
Problem 4 calculations to minimize the give two dimensional function using Powell's
Method or Quasi-Newton Method
--------------------------------------------------------------------------------------
"""
import numpy as np
from PowellMethod import powell_method
from Quasi_Newton import quasi_newton


def f1(x):

    F1 = (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

    return F1

def main1():

    Fmins = lambda x: f1(x)
    Fmaxs = lambda x: -1 * f1(x)

    L = np.array([-5.0, -5.0])
    U = np.array([5.0, 5.0])
    X0 = np.array([[-5., -2.], [5., -2.5], [-3., 3.8], [4.75, 1.8], [3., 2.]])
    Minimums = np.zeros(np.shape(X0))
    Maximums = np.zeros(np.shape(X0))

    F_mins = np.zeros(len(X0))
    F_maxs = np.zeros(len(X0))

    for i in range(len(X0)):
        Minimums[i, :], k1 = powell_method(Fmins, X0[i, :], L, U)
        F_mins[i] = Fmins(Minimums[i, :])
        Maximums[i, :], k2 = powell_method(Fmaxs, X0[i, :], L, U)
        F_maxs[i] = Fmaxs(Maximums[i, :])

    return np.around(Minimums, decimals=2), np.around(Maximums, decimals=2), F_mins, F_maxs


def main():

    Fmins = lambda x: f1(x)

    Fmaxs = lambda x: -1 * f1(x)

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


#    print("Minimums", Mins)
#    print("Maximums", Maxs)
#    print("Fmins", f_mins)
#    print("Fmaxs", f_maxs)
    print("Total no. of minimums", len(TotalMins))
    print("Total no. of maximums", len(TotalMaxs))