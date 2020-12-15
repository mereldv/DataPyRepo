# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:34:54 2020

@author: merel
"""

import numpy as np
import matplotlib.pyplot as plt

#%%
#5.2.1 Opdracht: Extra argumenten

# Rechte lijn
def f(x,a,b):
    return a+b*x

# Sinus
def g(x,amp,freq,offset):
    return offset + amp*np.sin(freq*x)

#Polynoom
def h(x,y,b,c):
    return b*x**2 + c*y**3 

## Simpele plotfunctie
# plot functie "func" over range "x"
# extra argumenten worden doorgegeven met *args
def my_plot(x,func,*args):
    plt.plot(x,func(x,*args))
    plt.show()
    
## Gebruik:
x_arr = np.linspace(-5.,5.)
#%%
def f(farg, *args, **kwargs):
    print("Het formele argument is", farg)
    print("De extra argumenten zijn:")
    for arg in args:
        print(arg)
    print("De keyword argumenten zijn:")
    for key in kwargs:
        print("  de key",key,"met argument",kwargs[key])
        if key == 'my_name':
            print("Mijn naam is", kwargs[key])
            
## Aanroepen van bovenstaande functie:
f("Aap", "Noot", "Mies", arg4="Wim", my_name="Zus", arg5="Merel")
# in bovenstaande aanroep zijn:
# Formeel argument   "Aap"
# Extra   argumenten "Noot" en "Mies"
# Keyword argumenten "Wim" bij keyword arg4, en "Zus" bij my_name
#%%
#5.4.1 Opdracht: Argumenten aan functies sturen
def f(a,b,c):
    print("a:",a)
    print("b:",b)
    print("c:",c)
"""    
# Normaal aanroepen:
f("Aap","Noot","Mies")

# Met *args
args = ("Noot","Mies")
f("Aap",*args)

# Met **kwargs
kwargs = {"c" : "Noot","b" : "Mies"} # Dit is een nieuw type object: dictionary
f("Aap",**kwargs)
"""
# Mix van beide, let op de volgorde!
args = ("Mies",)
kwargs = {"c" : "Noot"}
f("Aap",*args,**kwargs)

#%%
#5.4.2 Opdracht: Plotten

def h(x,y):
    z = x*y
    return z 

k = h(x_arr,3)

sig_x = [0,0.05,0.05,0.05,0.05,0.05]
sig_y = [0.03] *6
 

def my_plot(x,y, xlabel, ylabel,xerror=None, yerror=None, xrange=None, yrange=None,title=None, save=None):
    plt.xlim(xrange)
    plt.ylim(yrange)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.errorbar(x,y, xerr = xerror, yerr = yerror)
    if save == None:
        plt.show()
    elif type(save) == str:
        plt.savefig(save + ".png")
    else:
        print("Save moet een string zijn")


x_arr = [0,1,2,3,4,5] 
x_arr = np.array(x_arr)


s = my_plot(x_arr,k,"x-as","y-as",sig_x,sig_y,(0, 7),(0, 7),"Hoi")    

#%%
#5.4.3 Opdracht: Machtreeksen

x = np.arange(0,5)
A_n = np.arange(0,10) 

def MachtReeks(x, A_n, y_0 = 0, x_0 = 0):
    result = y_0
    for n in range(len(A_n)): 
        result += A_n[n]*(x-x_0)**n
    plt.plot(x,result) 
    plt.show()
    return result
    
    
resultaat = MachtReeks(x,A_n,2,4)
print(resultaat) 
  
#plt.plot(x,resultaat) 
#plt.show() 


#%%



