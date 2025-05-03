# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 09:10:20 2024

@author: diego
"""

import matplotlib.pyplot as plt
import numpy as np

# Función
def f(x):
    y = x**4 + 2*x**3*np.sin(x) - 3*x**2 + 4*x*np.cos(x) - 5
    return y

# Primera derivada
def fPrima(x):
    yPrima = 4*x**3 + 6*x**2*np.sin(x) + 2*x**3*np.cos(x) - 6*x + 4*np.cos(x) - 4*x*np.sin(x)
    return yPrima

# Segunda derivada
def fBiPrima(x):
    yBiPrima = 12*x**2 + 12*x*np.sin(x) + 4*x**2*np.cos(x) + 6*x**2*np.cos(x) - 6 - 8*np.sin(x) - 4*x*np.cos(x)
    return yBiPrima

# Rango de valores
x = np.arange(-5, 10, .2)

# Gráfica de la función
plt.plot(x, f(x), label="f(x)")
plt.plot(x, fPrima(x), label="f'(x)")
plt.plot(x, fBiPrima(x), label="f''(x)")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Función y sus derivadas')
plt.legend()
plt.grid()
plt.show()
