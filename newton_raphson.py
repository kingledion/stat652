# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 14:39:07 2016

@author: dhartig
"""

from math import exp

# USER INPUTS SECTION
# input function f as a function of x
def f(x):
        return exp(x) - 4
        
#Derivative of f
def dfdx(x):
        return exp(x)
        
# number of iterations
it = 10

# initial guess
x_n = 2


# perform iteration

x_n = float(x_n)

for i in range(it):
    x_nplus = x_n - f(x_n)/dfdx(x_n)
    f_str = "e^({0:2f}) - 4".format(x_n)
    dfdx_str = "e^({0:2f})".format(x_n)
    print("Iteration {4}: {0:.2f} = {1:.2f} - {2} / {3}".format(x_nplus, x_n, f_str, dfdx_str, i))
    x_n = x_nplus

print("Value of x_n: {0:.5f}".format(x_n))

