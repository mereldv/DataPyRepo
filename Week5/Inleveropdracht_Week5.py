# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 09:39:52 2020

@author: merel
"""

from math import pi, sin
import numpy as np
from matplotlib import pyplot as plt

#%%
#FOURIERREEKSEN
def fourierReeks(t, A_n, f_0, t_0 = 0, phi_n = None):
    if phi_n == None:
        phi_n = [0] * len(A_n) # Dit maakt een lijst van nullen precies even lang als A_n
    if len(A_n) != len(phi_n):
        print("phi_n en A_n zijn niet even lang!")
        return # Dit returnt een nonetype en dat gooit een flinke error als je de waarde van deze functie ergens gebruikt
    result = 0
    for n in range(len(A_n)):
        result += A_n[n] * sin(n*2*pi*f_0*(t-t_0)+phi_n[n])
    return result

print(fourierReeks(0.25, [1, 2], 1))
#%%
#TESTFUNCTIES 
def drieHoeksGolf(t, f_0 = 0): # Hoe denk je om te gaan met f_0? Nou, dit is denk ik wel een aardige oplossing.
    return 4 * abs(f_0*t + 0.25 - np.floor(f_0*t + 0.75)) - 1

def zaagTand(t, f_0 = 0):
    return f_0 * t - np.floor(f_0 * t) - 0.5

t = np.linspace(0, 0.5)
D = drieHoeksGolf(t, 2)
Z = zaagTand(t, 2)
S = []
for i in t:
    S.append(sin(2*pi*2*i))

plt.plot(t, D)
plt.plot(t, Z)
plt.plot(t, S)

plt.show()
#%%
#CONVERGENTIE

import numpy as np

def fourierReeks(t, A_n, f_0 = 1, t_0 = 0, phi_n = None):
    if phi_n == None:
        phi_n = [0] * len(A_n) # Dit maakt een lijst van nullen precies even lang als A_n
    if len(A_n) != len(phi_n):
        print("phi_n en A_n zijn niet even lang!")
        return # Dit returnt een nonetype en dat gooit een flinke error als je de waarde van deze functie ergens gebruikt
    result = 0
    for n in range(len(A_n)):
        result += A_n[n] * sin(n*2*pi*f_0*(t-t_0)+phi_n[n])
    return result

def drieHoeksGolf(t, f_0 = 1): # Hoe denk je om te gaan met f_0? Nou, dit is denk ik wel een aardige oplossing.
    return 4 * abs(f_0*t + 0.25 - np.floor(f_0*t + 0.75)) - 1

def zaagTand(t, f_0 = 1):
    return f_0 * t - np.floor(f_0 * t) - 0.5

def D_n(n):
    if n % 2 == 0:
        return 0
    else:
        l = 8/(np.pi**2)
        r_macht = (n-1)/2
        r = ((-1)**r_macht)
        deler = n**2
        return l * r / deler
    
def Z_n(n):
    if n > 0:
        return -1*((n*pi)**-1)
    elif n < 0:
        print("n moet op zijn minst 0 zijn")
    else:
        return 0

n = 1000
t = np.linspace(0, 1, num=1000)

D_coef = []
Z_coef = []
for i in range(n):
    D_coef.append(D_n(i))
    Z_coef.append(Z_n(i))

fourier_D, fourier_Z = [], []
for i in t:
    fourier_D.append(fourierReeks(i, D_coef))
    fourier_Z.append(fourierReeks(i, Z_coef))
    
D, Z = [], []
for i in t:
    D.append(drieHoeksGolf(i))
    Z.append(zaagTand(i))

plt.subplots_adjust(wspace=0.3, hspace=0.6)
plt.subplot(221)
plt.xlabel("$t$")
plt.ylabel("$Fourier van D")
plt.title("Benadering D")
plt.plot(t, fourier_D)
plt.subplot(222)
plt.xlabel("$t$")
plt.ylabel("$DrieHoeksgolf$")
plt.title("Werkelijke D")
plt.plot(t, D)

plt.subplot(223)
plt.title("Benadering Z")
plt.xlabel("$t$")
plt.ylabel("$Fourier van Z$")
plt.plot(t, fourier_Z)
plt.subplot(224)
plt.xlabel("$t$")
plt.ylabel("$Zaagtand$")
plt.title("Werkelijke Z")
plt.plot(t, Z)
plt.show() 

#Kwadratisch verschil
def kwadratenverschil(l_1, l_2):
    if len(l_1) == len(l_2):
        return sum([(l_1[i]-l_2[i])**2 for i in range(len(l_1))])
    else:
        print("Om een kwadratisch verschil uit te rekenen moeten de twee lijsten even lang zijn!")
        return

#print(kwadratenverschil(fourier_D, D))

def hulploop(n):
    t = np.linspace(0, 1, num=1000)

    D_coef = [D_n(i) for i in range(n)]
    Z_coef = [Z_n(i) for i in range(n)]

    fourier_D = [fourierReeks(i, D_coef) for i in t]
    fourier_Z = [fourierReeks(i, Z_coef) for i in t]

    D = [drieHoeksGolf(i) for i in t]
    Z = [zaagTand(i) for i in t]
    return kwadratenverschil(fourier_D, D), kwadratenverschil(fourier_Z, Z)

    
with open('somefile.txt', 'w') as the_file:
    for i in range(1, 1000):
        temp = hulploop(i)
        payload = str(i) + ";" + str(temp[0]) + ";" + str(temp[1]) + "\n"
        the_file.write(payload)
        print(i)

#%%
#Deze cel is aangemaakt, zodat je niet voor elke plot opnieuw de berekening hoeft uit te voeren. Deze berekening kan namelijk heel 
#lang duren als je een hoge waarde van n neemt . 
with open('somefile.txt') as infile:
    lines = infile.readlines()
    lines = [line.strip().split(";") for line in lines]
    
lines = [[int(line[0]), float(line[1]), float(line[2])] for line in lines]

n_termen = [line[0] for line in lines]
kw_versch_D = [line[1] for line in lines]
kw_versch_Z = [line[2] for line in lines]

for line in lines:
    print(line)

plt.loglog(n_termen, kw_versch_D, label ="Kwadratisch verschil DrieHoeksfunctie")
plt.loglog(n_termen, kw_versch_Z, label ="Kwadratisch verschil Zaagtand")
plt.xlabel("$N$")
plt.ylabel("$Kwadratisch verschil$")
plt.title("Kwadratisch verschil naar n")
plt.legend(loc='lower left')
plt.show()
#%%
#CONCLUSIES 

    