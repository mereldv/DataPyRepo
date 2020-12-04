# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 09:34:01 2020

@author: merel
"""
import numpy as np


#Zelfde resultaat


array1a  = np.array([0,1,2,3,4,5])
array1b  = np.arange(6)         
print(array1a)
print(array1b)

kopie_arr = array1a.copy() #twee verschillende arrays
same_arr = array1b     #zelfde
print(kopie_arr)
print(same_arr)

"""
#grid
grid1 = np.arange(0.,5.,0.25)        # 0 TOT 5 met stapjes van 0.25
grid2 = np.linspace(0.,5.,num=20)    # 0 TOT EN MET 5, 20 equidistante getallen
print(grid1)
print(grid2)
"""
