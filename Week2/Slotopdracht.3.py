# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:59:18 2020

@author: merel
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1.0,1.0,num=100)
y = np.linspace(-1.0,1.0,num=100)

xv,yv = np.meshgrid(x,y)

def berglandschap1(X,Y):
	np.random.seed(4321)
	temp = X.copy()*0
	for i in range(10):
		temp += bivariate_normal(X, Y, 0.1+np.random.random_sample(), 0.1+np.random.random_sample(), np.random.random_sample(), np.random.random_sample())

	return temp

def bivariate_normal(X, Y, sigmax=1.0, sigmay=1.0,
                     mux=0.0, muy=0.0, sigmaxy=0.0):
    """
    Bivariate Gaussian distribution for equal shape *X*, *Y*.
    See `bivariate normal
    <http://mathworld.wolfram.com/BivariateNormalDistribution.html>`_
    at mathworld.
    
    met dank aan Tom de Vries en Sander de Graaf , nov. 2019
    """
    Xmu = X-mux
    Ymu = Y-muy

    rho = sigmaxy/(sigmax*sigmay)
    
    z = Xmu**2/sigmax**2 + Ymu**2/sigmay**2 - 2*rho*Xmu*Ymu/(sigmax*sigmay)
    
    denom = 2*np.pi*sigmax*sigmay*np.sqrt(1-rho**2)
    
    return np.exp(-z/(2*(1-rho**2))) / denom
		
Z = berglandschap1(xv,yv)

use_imshow = 1

###########################################
# Voeg hier code toe om contour te tekenen 
###########################################
plt.figure()
plt.subplot(121)


numlevels = np.linspace(-4, 4, num=20) 
plt.contour(x, y, Z, levels = numlevels)

plt.subplot(122)


###########################################
#      Slot code om contour te tekenen     
###########################################

if use_imshow == 1:
	plt.imshow(Z,
			   interpolation='none',
			   extent = [x.min(),x.max(),y.min(),y.max()],
			   cmap="terrain",
			   origin="lower")
plt.savefig("Plaatje.png")
plt.title("DATA-Py heuvels")
plt.show()

  

m = np.matrix(Z)
print(m.max(), m.min())
