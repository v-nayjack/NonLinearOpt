# Created by Vinay Jakkali on 12/8/2019

"""
--------------------------------------------------------------------------------------
Include code description here:

--------------------------------------------------------------------------------------
"""
import numpy as np


def bfgs(Hk, gamma_k, delta_k):

    H_k = np.copy(Hk)

    Gamma_k = np.copy(gamma_k)

    Delta_k = np.copy(delta_k)

    A = np.dot(np.transpose(Delta_k), Gamma_k)

    B = np.dot(Delta_k, np.transpose(Delta_k))

    C = np.dot(np.dot(H_k, Gamma_k), np.transpose(Delta_k))

    D = np.dot(np.dot(Delta_k, np.transpose(Gamma_k)), H_k)

    E = np.dot(np.transpose(Gamma_k), np.dot(H_k, Gamma_k))

    Second = (C + D)/ A

    Third = (1 + (E/A)) * (B/A)

    H_k1 = H_k - Second + Third

    return H_k1





