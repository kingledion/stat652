#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:10:44 2017

@author: dhartig
"""
from matplotlib import pyplot as plt

X = [x/100-1 for x in range(201)]
Y = [(1/16)*(0.0225*x**4-0.2*x**3-0.34*x**2+0.8*x+1) for x in X]

plt.plot(X,Y)
plt.show()