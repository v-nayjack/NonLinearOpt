# Created by Vinay Jakkali on 12/8/2019

"""
--------------------------------------------------------------------------------------
Broyden-Fletcher-Goldfarb-Shanno(BFGS) Update

INPUT:
    Hk : It is a matrix of size NxN. It is an approximation of the inverse of the
    Hessian. Here it contains NxN values at 'k' iteration of Quasi-Newton method

    gamma_k - It is an array of size Nx1 containing G(k+1) - G(k) values, where 'G' is the
    gradient array obtained from Gradient function

    delta_k - It is an array of size Nx1 containing X(k+1) - X(k) values, where 'X' contains
    the values of N variables in 'x' which are updated

OUTPUT:
    1. Returns a matrix H(k+1) of size NxN, It is an approximation of the inverse of the
    Hessian. Here it contains NxN values at 'k+1' iteration of Quasi-Newton method
--------------------------------------------------------------------------------------
"""
import numpy as np


def bfgs(Hk, gamma_k, delta_k):

    H_k = np.copy(Hk)

    Gamma_k = np.copy(gamma_k)

    Delta_k = np.copy(delta_k)

    A = np.dot(np.transpose(Delta_k), Gamma_k)


    if A[0] <= 0.:
        return H_k


    B = np.dot(Delta_k, np.transpose(Delta_k))


    C = np.dot(np.dot(H_k, Gamma_k), np.transpose(Delta_k))


    D = np.dot(np.dot(Delta_k, np.transpose(Gamma_k)), H_k)


    E = np.dot(np.transpose(Gamma_k), np.dot(H_k, Gamma_k))


    Second = (C + D)/ A

    Third = (1 + (E/A)) * (B/A)

    H_k1 = H_k - Second + Third

    return H_k1





