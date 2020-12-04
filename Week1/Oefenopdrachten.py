# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 13:49:48 2020

@author: merel
"""

"""
print("Hello World!")
print(1 + 1)

#Oefenopdracht 1: Python als rekenmachine
v0 = 25 #m/s
t = 2 #s
g = 9.81 #m/s**5
y = v0*t - 1/2*g*t**2
print(y)


#Complexe getallen
a = complex(3,2)
print(a)
"""

"""
#Oefenopdracht2: Controleren van bovenstaande functie
def polynoom(a, b, c, x):
    y = a*x**2 + b*x + c
    return y

i = 1
j = 2
k = 3
z = 1

waarde = polynoom(i,j,k,z)     
print("waarde =", waarde)

"""


#Oefenopdracht: Begrip van variabelen binnen en buiten een functie
def polynoom(a,b,c,x):
    print('binnen functie geldt a =', a)
    y = a*x**2 + b*x + c
    return y

a = 3.14
f = polynoom(x=3.14, a=1, b=1, c=1)
print('buiten functie geldt a =', a)
