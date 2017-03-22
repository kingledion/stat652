# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 14:39:07 2016

@author: dhartig
"""


# input function f as a function of x
def f(x):
        return (1/16)*(0.09*x**3-0.6*x**2-0.68*x+0.8)
        
#Derivative of f
def dfdx(x):
        return (1/16)*(0.27*x**2-1.2*x-0.68)
        
# number of iterations
it = 10

# initial guess
x_n = 0.6


# perform iteration
x_n = float(x_n)
for i in range(it):
    x_nplus = x_n - f(x_n)/dfdx(x_n)
    print("Iteration {1}: {4:.2f} = {0:.2f} - {2:.2f}/{3:.2f}".format(x_n, i, f(x_n), dfdx(x_n), x_nplus))
    x_n = x_nplus

print("Value of x_n: {0:.5f}".format(x_n))

