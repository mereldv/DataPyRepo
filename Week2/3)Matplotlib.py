# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:51:49 2020

@author: merel
"""

import matplotlib.pyplot as plt
import numpy as np


#Oefenopdracht A,B,C,D
x = np.linspace(0.,2*np.pi,num=100)
y = np.sin(x)       
y2 = np.cos(x)                 

plt.xlim(0.,2*np.pi)
plt.ylim(-1.2,1.2)   
#plt.figure()               
plt.plot(x,y,'r-.')   
plt.plot(x,y2,'y-.')
plt.xlabel("mooie x-as")
plt.ylabel("mooie y-as")
plt.title("Mijn adembenemende grafiek")


#plt.axes().set_aspect(1)
#plt.figure()
#plt.plot(y,y2)


