# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 12:33:53 2020

@author: merel
"""
"""
#While-loop
y0 = 0     # beginhoogte
v0 = 25    # beginsnelheid
g = 9.81   # gravitatieconstante
t = 0.     # begintijd
dt = 0.25  # tijdstap

while t<= 5:
    y = y0 + v0*t - 0.5*g*t**2
    print(t, y)
    
    t = t + dt
"""


"""  
#If-loop
def N(x):
    if x<0:
        return 0.
    elif x<1:
        return x
    elif 1<=x<2:
        return 2-x
    else: 
        return 0.

waarde = N(1.5)
print(waarde)
"""


"""
#Oefenopdracht
if "abc" < "defg": 
    print("yay")
"""
"""
#Oefenopdracht
a = complex(3,6)
b = complex(6,3)
if a != b: 
    print("klopt")
"""


#Oefenopdracht
def ExclusiveOr(arg1, arg2):
    if (arg1 + arg2) == 1:
        return True
    else: 
        return False 

A = ExclusiveOr(16 == 16, 1 == 2)
print(A)

#For-loop
for k in range(5):
    print(k)
        
    
