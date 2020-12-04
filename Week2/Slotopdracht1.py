# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 09:22:59 2020

@author: merel
"""
import numpy as np
import matplotlib.pyplot as plt


#%%
#Maak een grafiek van de functie f waarbij je alleen het deel plot metx∈[−4π,4π]:

    
f= []  
x = np.linspace(-4*np.pi, 4*np.pi, num=1000)
for ding in x:
    if np.cos(ding) > 0:
        f.append(np.cos(ding)**2)
    else:
        f.append(np.cos(ding))


    
plt.plot(x,f)
plt.show()
#%%
x = np.arange(-4*np.pi, 4*np.pi) 
y = np.cos(x)

masker = y > 0
nieuwe_lijst = y[masker]
print(nieuwe_lijst)

masker2 = y <= 0
nog_een_lijst = y[masker2]
print(nog_een_lijst)

for ding in nieuwe_lijst:
    z = np.cos(nieuwe_lijst)**2
for ding in nog_een_lijst:
    z = np.cos(nog_een_lijst)

plt.figure()
plt.plot(x,z)
plt.show()
