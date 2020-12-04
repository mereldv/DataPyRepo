# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 14:17:05 2020

@author: merel
"""

#Blz 27

import numpy as np
import matplotlib.pyplot as  plt

# Maak arrays voor r en theta
th = np.linspace(-0,2*np.pi,num=100)
r  = np.linspace(1E-5,1.0)       # r = 0 is overgeslagen om singulariteiten te voorkomen.

# Meshgrid
rv, thv = np.meshgrid(r,th)

#Genereer functiewaarden in 2d-array 'img'. 
#In dit geval de tweede Bessel-functie en een hoekafhankelijke oscillatie.
fr = np.sin(rv)/rv**2 - np.cos(rv)/rv
fth = np.cos(4*thv)
img = fr*fth

#Plot eerst met imshow:
plt.figure("Figuur 1")
plt.imshow(img, extent = [r.min(),r.max(),th.min(),th.max()])
plt.colorbar()
plt.axes().set_aspect(1/(2*np.pi)) # Zo wordt 2*pi langs theta-as even lang als 1 langs de r-as.

plt.xlabel(r"$r$")
plt.ylabel(r"$\theta$")
plt.show()

#Construeer xv en yv uit rv en thv.
xv = rv * np.cos(thv)
yv = rv * np.sin(thv)

#Plot nu de geparameteriseerde plot met plt.pcolormesh()
#Nu wordt de hoekafhankelijkheid `uitgerold`:
plt.figure("Figuur 2")
plt.pcolormesh(xv,yv,img)
plt.colorbar()
plt.axes().set_aspect('equal')
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.show() 

