# Created by Vinay Jakkali on 12/9/2019

"""
--------------------------------------------------------------------------------------
Include code description here:

--------------------------------------------------------------------------------------
"""
import numpy as np


def f(x):

    Func = (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

    return Func

def main():

    X0 = np.array([0.5, 1.3])
    L = np.array([-5.0, -5.0])
    U = np.array([5.0, 5.0])
    x = np.linspace(L[0], U[0], 11)
    y = np.linspace(U[1], L[1], 11)
    X, Y = np.meshgrid(x, y)






if __name__ == '__main__':
    main()



