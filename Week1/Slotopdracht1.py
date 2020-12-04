# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 13:19:12 2020

@author: merel
"""

#Conversie van Fahrenheit naar Celsius
for F in range(-10,101,5):
    C = ((5/9)*F - 32*(5/9))
    if C > 0:
        print(F, "Het vriest niet.") 
    if C <= 0:
        print(F, "Het vriest.")  
        
