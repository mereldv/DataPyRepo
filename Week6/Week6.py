# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 08:56:03 2020

@author: merel
"""
import numpy as np
import timeit
#%%
# vind alle even getallen uit een random lijst op twee manieren
import time

n = 1000000                                   # aantal random getallen
random_nrs = np.random.randint(100,size=n)  # n random int tussen 0 en 99

start_tijd1 = time.time()                   # start de tijd voor methode 1
even_nrs1 = []                              # maak lege lijst voor even getallen                 
for element in random_nrs:                  # loop door de hele lijst
    if element % 2 == 0:                    # als een getal even is (% 2 = 0)
        even_nrs1.append(element)           # voeg het getal toe aan de lijst even_nrs1
eind_tijd1 = time.time()                    # stop de tijd voor methode 1
verstreken_tijd1 = eind_tijd1-start_tijd1   # bereken de verstreken tijd
print(f'methode 1 duurt: {verstreken_tijd1:.4f} sec')

start_tijd2 = time.time()                    # start de tijd voor methode 2
masker_even_getallen = random_nrs % 2 == 0   # maak een masker voor even getallen
even_nrs2 = random_nrs[masker_even_getallen] # gebruik het masker
eind_tijd2 = time.time()                     # stop de tijd voor methode 2
verstreken_tijd2 = eind_tijd2-start_tijd2    # bereken de verstreken tijd
print(f'methode 2 duurt: {verstreken_tijd2:.4f} sec')

#Hint:  gebruik a =list(a) of b = np.array(b)
#%%

# De functie timeit heeft een input statement (stmt) nodig, een setup (setup), 
# en een aantal herhalingen (number)
# De output van de functie is dan de duur van het aantal herhalingen in seconden
# verstreken_tijd = timeit.timeit(stmt,setup,number=10000)

# De code van de setup wordt 1 keer, aan het begin, gerund en de code in de
# stmt wordt het aantal ingevoerde herhalingen gerunt.


# Het stmt staat geheel tussen ''' ''', en bevat alleen het aanroepen van de functie

# We doen niks met de output (return), slaan die niet op in een variabele.
stmt1 = '''
methode1(n)
'''
# De setup bevat eventuele initiele parameters en de definitie van de functie(s)
# Let op: de setup moet ook het importeren van benodigde packages bevatten.
setup1 = '''
import numpy as np

n = 100                                     # aantal random getallen
random_nrs = np.random.randint(100,size=n)  # n random int tussen 0 en 99

def methode1(n):
    even_nrs1 = []                          # maak lege lijst voor even getallen                 
    for element in random_nrs:              # loop door de hele lijst
        if element % 2 == 0:                # als een getal even is (% 2 = 0)
            even_nrs1.append(element)       # voeg het getal toe aan de lijst even_nrs1
    return even_nrs1
''' 
# Idem voor methode 2:
stmt2 = '''
methode2(n)
'''
setup2 = '''
import numpy as np

n = 100                                     # aantal random getallen
random_nrs = np.random.randint(100,size=n)  # n random int tussen 0 en 99

def methode2(n):
    masker_even_getallen = random_nrs % 2 == 0  # maak een masker voor even getallen
    even_nrs2 = random_nrs[masker_even_getallen] # gebruik het masker
    return even_nrs2
''' 

# Nu gaan we de snelheidsmeting uitvoeren
k = 10000
methode1_tijd = timeit.timeit(stmt1,setup1,number=k)
methode2_tijd = timeit.timeit(stmt2,setup2,number=k)

# En de resulaten printen
print(f'methode 1 duurt: {methode1_tijd:.4f} sec bij {k:.1e} herhalingen')
print(f'methode 2 duurt: {methode2_tijd:.4f} sec bij {k:.1e} herhalingen')
#%%
#OEFENOPDRACHT
#A
stmt1 = '''
oudste_notatie()
'''
stmt2 = ''' 
verouderde_notatie()
'''
stmt3 = ''' 
nieuwe_notatie()
'''
stmt4 = ''' 
nieuwste_notatie()
'''
setup1 = '''
x = 'awesome'
def oudste_notatie():
    print('hello ' + x + ' world')
'''
setup2 = '''
x = 'awesome'
def verouderde_notatie():
    print('hello %s world' % x)  
'''
setup3 = '''
x = 'awesome'
def nieuwe_notatie():
    print('hello {} world'.format(x))
'''
setup4 = '''  
x = 'awesome'
def nieuwste_notatie():
    print(f'hello {x} world') 
'''
k = 1
methode1_tijd = timeit.timeit(stmt1,setup1, number = k)
methode2_tijd = timeit.timeit(stmt2,setup2, number = k)
methode3_tijd = timeit.timeit(stmt3,setup3, number = k)
methode4_tijd = timeit.timeit(stmt4,setup4, number = k)

print(f"De tijd is {methode1_tijd:.6f}")
print(f"De tijd is {methode2_tijd:.6f}")
print(f"De tijd is {methode3_tijd:.6f}")
print(f"De tijd is {methode4_tijd:.6f}") 

#B
stmt1 = '''
eerste() 
'''
stmt2 = ''' 
tweede()  
'''
setup1 = '''
import numpy as np
a = np.arange(100) 
def eerste():
    print(a)
'''
setup2 = '''
b = [*range(100)]
def tweede():
    print(b)  
'''
k = 1
methode1_tijd = timeit.timeit(stmt1,setup1, number = k)
methode2_tijd = timeit.timeit(stmt2,setup2, number = k)

print(f"De tijd is {methode1_tijd:.6f}")
print(f"De tijd is {methode2_tijd:.6f}")


