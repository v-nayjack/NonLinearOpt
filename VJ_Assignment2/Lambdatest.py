# Created by Vinay Jakkali on 12/6/2019

"""
--------------------------------------------------------------------------------------
Include code description here:

--------------------------------------------------------------------------------------
"""



Func = lambda x, y: -4 * x + x ** 2 - y - x * y + y ** 2
X0 = [2.55, 1.75]

print(list(map(Func, X0)))
