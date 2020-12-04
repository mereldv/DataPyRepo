# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 11:26:00 2020

@author: merel
"""

import numpy as np

data = np.genfromtxt("Voorbeeld.txt", delimiter='\t')

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

f =  open("Voorbeeld.txt", "r")
block = f.readlines()
words = line.split(sep='\t')
functie_aanroep = is_number(words[-1])

para = []
counthashtag = 0 
countgetallen = 0
for line in block:
  for elem in line:
      if elem[0] == '#':
          counthashtag += 1
          if functie_aanroep == True:
              countgetallen += 1
              getal = float(words[-1])
              para.append(getal)
              
print("Er zijn",counthashtag,"commentaarregels gevonden")
print("Er zijn",countgetallen,"getallen gevonden")
print(para)

