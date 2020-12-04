# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:10:39 2020

@author: merel
"""

"""
Script om alle items in een bestand als string te interpreteren
Zo'n string bevat geen spaties of tab's.
Maak zelf je eigen oefen-bestand aan.
"""
f =  open("MijnEersteBestand.txt", "r")
block = f.readlines()

data = []   #  een lege Python lijst
for line in block:
    data.append( line.split() )  
# check data na runnen script


