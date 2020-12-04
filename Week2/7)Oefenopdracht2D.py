# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:48:36 2020

@author: merel
"""
#blz 26

import numpy as np
import matplotlib.pyplot as plt


# Opdracht A

x = np.linspace(-1.0,1.0)
y = np.linspace(-1.0,1.0)
xv, yv = np.meshgrid(x,y, indexing ='ij')
hyperbool = xv**2 - yv**2
print(hyperbool)

plt.imshow(hyperbool, interpolation ='none',cmap = 'seismic', extent = [x.min(),x.max(),y.min(),y.max()])
plt.colorbar()
plt.show()



"""
# Opdracht B

x = np.linspace(-1.0,1.0)
y = np.linspace(-1.0,1.0)
xv, yv = np.meshgrid(x,y, indexing ='xy')
hyperbool = xv / yv
print(hyperbool)

plt.xlabel("mooie x-as")
plt.ylabel("mooie y-as")
plt.title("Mijn grafiek")

plt.imshow(hyperbool, interpolation ='bicubic',cmap = 'seismic', extent = [x.min(),x.max(),y.min(),y.max()], clim=(-1.5,1.5))
plt.colorbar()
plt.show()
"""

""" 
y = np.linspace(-1.0,1.0)

xv, yv = np.meshgrid(x,y, indexing ='xy')
f = np.sin(4*xv*np.pi)**2*yv**2

plt.imshow(f,interpolation = "none", extent = [xv.min(),xv.max(),yv.min(),yv.max()], clim=(0,0.8))
plt.colorbar() 
plt.show() #Moet deze erbij?

gemiddelde_yv = f.mean(axis=1) 
gemiddelde_xv = f.mean(axis=0)
plt.plot(gemiddelde_yv) #Hij laat niks zien? 
plt.plot(gemiddelde_xv) 
plt.show()
"""
