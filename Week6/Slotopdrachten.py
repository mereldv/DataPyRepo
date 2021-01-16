# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 11:01:44 2020

@author: merel
"""
import numpy as np
import matplotlib.pyplot as plt

#SLOTOPDRACHT 1
#6.3.1    Verbeter het script voor het vinden van pi

def berekenPi(N):
    lijst = []
    x = np.random.random(size=N)
    y = np.random.random(size=N)
    r = (x**2 + y**2)**0.5
    for i in r:
        if i<1:
            lijst.append(1)
        else:
            lijst.append(0)
    gemiddelde = np.mean(lijst)
    pi = gemiddelde*4/r**2
    return pi

abs_versch = []
N = []
for n in range(10, 10**2, 10):
    N.append(n)
print(N)

for m in N:
    berekend = berekenPi(m)
    abs_versch.append(abs(np.pi - berekend))
    
    
print(type(abs_versch), type(N))
print(len(abs_versch), len(N))    
plt.plot(N, abs_versch)


    
