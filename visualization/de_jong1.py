#!/usr/bin/env python
# coding: utf-8

"""
https://en.wikipedia.org/wiki/Rastrigin_function

Non-convex function for testing optimization algorithms.
"""

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import math
import matplotlib.pyplot as plt
import numpy as np

def deJong1(*X):
        return sum(x**2 for x in X)

if __name__ == '__main__':
    X = np.linspace(-4, 4, 200)    
    Y = np.linspace(-4, 4, 200)    

    X, Y = np.meshgrid(X, Y)

    Z = deJong1(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.plasma, linewidth=0, antialiased=False)    
    plt.savefig('visualization/de_jong1.png')