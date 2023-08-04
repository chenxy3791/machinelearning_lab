# -*- coding: utf-8 -*-
"""
Created on Sun May 27 11:14:17 2018

@author: chen
"""

import numpy as np
import matplotlib.pyplot as plt
#from pylab import *

x = np.linspace(0, 5, 10)
y = x ** 2

fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)

axes.plot(x, y, 'r')

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')

plt.show()

x = np.linspace(-10, 10, 100)
f_original    = x*np.sin(x)
f_order6_appr = x*x + (-1/6)*x**4 + (1/120)*x**6
fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)

axes.plot(x, f_order6_appr, 'r')
axes.plot(x, f_original, 'b')

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('6th-order approximation of f(x) = x*sinx')
axes.grid(True)

plt.axis([-10,10,-5,9])  
plt.show()