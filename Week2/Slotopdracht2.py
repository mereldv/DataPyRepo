# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:15:12 2020

@author: merel
"""

#Maak een figuur van 2-bij-2 plots waarin net als in het voorbeeld met de drie plotjes de xmarkering weggelaten is voor figuren 
#die niet onderaan staan. 
#Laat ook de y-markering weg voor figuren die niet helemaal links staan. 
#Plots moeten er als volgt uit zien: 
#Voor elke plot is het bereik voor x gelijk aan [0, 1]. 
#In elke plot moet x**α komen staan. 
#In linksboven voor α = 0.125, 0.25, 0.5, 1, in rechtsboven α = 1, 1.5, 2, in linksonder α = 1, 2, 3, 4 en rechtsonder
#α = 0.1, 1, 10. 
#(TIP: Plot eerst de figuren, daarna pas de styling.)

import numpy as np
import matplotlib.pyplot as plt


f, axarr = plt.subplots(2, 2, sharex='col', sharey='row')

x = np.linspace(0,1)

a = [0.125, 0.25, 0.5,1]
for ding in a:
    axarr[0,0].plot(x,x**ding)

a = [1,1.5,2]     
for ding in a:
    axarr[0,1].plot(x,x**ding)   

a = [1,2,3,4]     
for ding in a:
    axarr[1,0].plot(x,x**ding)
                           
a = [0.1,1,10]     
for ding in a:
    axarr[1,1].plot(x,x**ding)     

