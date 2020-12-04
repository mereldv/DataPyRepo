# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:48:31 2020

@author: merel
"""
#blz 24

import matplotlib.pyplot as plt
import numpy as np

"""
#Opdracht b

t = np.linspace(0, 2*np.pi, num=100)
x = 16*np.sin(t)**3
y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)
plt.axes().set_aspect('equal')
plt.figure()
plt.plot(x,y)
"""


#Opdracht c

#logaritmische schaal
x = np.linspace(0,5)
y = x*np.exp(x)
plt.yscale('log')
plt.plot(x,y)


#geen logaritmische schaal
x = np.linspace(0,5)
y = x*np.exp(x)
plt.figure()
plt.plot(x,y)



"""
#Opdracht d

x = np.linspace(0,2*np.pi, num=100)
y = np.cos(x)
y2 = np.sin(x)

plt.figure()
plt.plot(x,y,'b', label = "Cosinus")
plt.plot(x,y2,'g', label = "Sinus")
plt.legend()
"""