# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:17:06 2020

@author: merel
"""
import numpy as np
import matplotlib.pyplot as plt

lijst = []

x = np.random.random(size=10**3)
y = np.random.random(size=10**3)
r = (x**2 + y**2)**0.5
print(r)

for i in r:
    if i<1:
        lijst.append(1)
    else:
        lijst.append(0)
print(lijst)

gemiddelde = np.mean(lijst)
print(gemiddelde)

pi = gemiddelde*4/r**2
print(pi)

y2 = np.pi - pi
plt.loglog(r,y2) 

