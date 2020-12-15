# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:30:45 2020

@author: merel
"""
#5.4.2 Opdracht: Plotten

import matplotlib.pyplot as plt 
import numpy as np

def h(x,y):
    z = x*y
    return z 

sig_x = [0,0.05,0.05,0.05,0.05,0.05]
sig_y = [0.03] 
 

def my_plot(x,y, xlabel, ylabel, xerror=None, yerror=None, xrange=None, yrange=None):
    plt.errorbar(x,y, xerr = xerror, yerr = yerror)
    plt.show() 

x_arr = [0,1,2,3,4,5] 
x_arr = np.array(x_arr)

k = h(x_arr,3)
s = my_plot(x_arr,k,"x-as","y-as",xerror=sig_x,yerror=sig_y)    

