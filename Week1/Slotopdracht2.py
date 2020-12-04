# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 13:21:37 2020

@author: merel
"""

#Fibonacci
def F(a, b):
    lijst1 = [a,b]
    while len(lijst1) <= 50:
        lijst1.append(lijst1[-1] + lijst1[-2])
    return lijst1

lijst = F(1.5, 2.5)
print(lijst)



