# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 12:21:57 2020

@author: merel
"""
import numpy as np
import matplotlib.pyplot as plt
#%%
#SLOTOPDRACHT 

"""
1: Genereren data
We zullen in deze opdracht onze bananen met behulp van de pseudo-random number generator
genereren. De bananen hebben een lengte L, diameter d, kromtestraal R en bruine stukken
van het oppervlakte met afmeting A. Kies voor normaalverdeelde statistiek met de parameters
(µL, σL) = (15.5, 1.0) cm, 
(µd, σd) = (35.0, 5.0) mm,
(µR, σR) = (20.0, 3.0) cm 
(µA, σA) = (2.2, 1.3) cm2

Zorg dat de statistiek voor A geen negatieve getallen bevat. Ga ervan uit dat
wanneer het oppervlakte A negatief wordt, de banaan geheel vrij is van smetten. Genereer 105
samples.
"""
#OPDRACHT 1
L = np.random.normal(15.5,1.0,size=10**5) #normaalverdeeld
d = np.random.normal(35.0,5.0,size=10**5)
R = np.random.normal(20.0,1.3,size=10**5)
A = np.random.normal(2.2,1.3,size=10**5)

for i in range(len(A)):
    if A[i] < 0:
        i = 0
#OPDRACHT 2
masker_d = d>=27 #minimum eisen voor goedkeuring op basis van d
a = np.mean(masker_d)*100
print("Afgekeurde bananen door dikte is",100-a,"procent")

#OPDRACHT 3
masker_L = L>=14
masker_Ld = masker_L * masker_d #minimum eisen voor goedkeuring op basis van L en d
b = np.mean(masker_Ld)*100
print("\nAfgekeurde bananen door dikte en lengte is",100-b,"procent")

#OPDRACHT 4
masker_A = A <= 4
masker_dLA = masker_d*masker_L*masker_A #minimum eisen voor goedkeuring op basis van L,d en A
afgekeurd = 0
I = 0
II = 0
Extra = 0
for i in range(len(A)):
    if not masker_dLA[i]:
        afgekeurd +=1
    elif R[i]>=1.25*L[i] and R[i]<=1.3*L[i] and A[i] <= 1:
        Extra += 1
    elif R[i]>=1.2*L[i] and R[i]<=1.4*L[i] and A[i] <= 2 and A[i]>1:
        I += 1
    else:
        II += 1
print("\nAfgekeurd", afgekeurd/len(A)*100,"procent")
print("Extra", Extra/len(A)*100,"procent")
print("I", I/len(A)*100,"procent")
print("II", II/len(A)*100,"procent") 



    





