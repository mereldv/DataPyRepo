# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 09:09:13 2020

@author: merel
"""
import numpy as np
import matplotlib.pyplot as plt

#%%

#3.1.1 Oefenopdracht: sorteren en reshapen

"""
Laat y = np.arange(30); np.random.shuffle(y). Verifieer de syntax en ga na wat de werking van np.random.shuffle() is. Waarom werkt y = np.random.shuffle(np.arange(30)) niet?
Schrijf een script wat y verandert in een gesorteerde 2 bij 15 array, waar de bovenste rij de 15
oneven getallen gesorteerd bevat en de onderste rij de 15 even getallen. Maak slim gebruik van
np.sort() en np.reshape().

""" 

y = np.arange(30)
np.random.shuffle(y)
#print(y) #alle getallen van y worden geshuffled.
origineely = np.sort(y) #sorteert de lijst weer
y2 = np.reshape(origineely, (15,2))
y3 = np.transpose(y2)  
##print(y3)
y4 = y3[::-1]   #rijen verwisselen

# bij z4 wordt gebruik gemaakt van 'slicing'; hierbij selecteer je een deel van een variable.
# je kunt een element uit een variabele selecteren met
# variable[index_nr]
# bijvoorbeeld:
##print(y[3]) # print het 4e element uit y (python begint bij 0 met tellen; vergelijk met de variable explorer!)
# uit een 2D array kun je ook elementen selecteren:
##print(z2[3,1]) # print het 4e element uit de 2e kolom
# slicing gebruikt deze coordinaten ook, maar dan om meerdere elementen te selecteren:
# variabele[start:stop:step]
# bijvoorbeeld:
##print(z1[0:29:2])   # print alle even getallen; begint bij 0e element, en selecteert in stappen van 2
# Een veelgebruikt slim trucje is om als stap -1 in te vullen, de elementen komen dan in omgekeerde volgorde aan bod
# door geen start en stop waarde in te vullen wordt de hele variable gebruikt
##print(z1[::-1])     # reeks wordt omgedraait

#%%
#3.2 Samenvoegen voorbeeld

## Maak 3 arrays
a  = np.arange(25).reshape(5,5)  # een 5 bij 5 matrix
b1 = np.arange(10).reshape(2,5)  # een 2 bij 5 matrix
b2 = b1.T                        # een 5 bij 2 matrix

# Dit gaat goed:
conc1 = np.concatenate((a,b1))
#print(conc1)

# Dit gaat mis, niet matchende dimensies
conc2 = np.concatenate((a,b2))
#print(conc2) 
# Met axis keyword wordt langs de tweede as gewerkt en lukt het wel
conc3 = np.concatenate((a,b2),axis=1)
# let op: python begint bij 0 met tellen, dus axis=1 is de tweede as
#%% For-loops voorbeeld 
""" 
Oefenenen met for-loops en matrices: 6 getallen, 2 groepjes van 3
ofwel 2 rijen en 3 kolommen; auteur:                FvH, nov 2019
"""

data = [1,2,3], [3,4,5]
# Dit is een tuple! Je mag er (..) omheen zetten dus data = ([1,2,3],[3,4,5]), 
# maar dat hoeft niet. Je mag er ook [..] omheen zetten, maar dan is data 
# geen tuple meer, maar een lijst. Voor dit voorbeeld maakt het niets uit.
# Het verschil tussen lijsten en tuples wordt in deze cursus niet behandeld.
print('data = ', data)
print('Gemiddelde van alle ALLE items = ', np.mean(data))
# In Python is er geen functie mean, maar in NumPy wel, vandaar np.mean

# Berekening van het gemiddelde van elk item apart gaat met een for-loop:
for item in data:
    print('gemiddelde van ', item, ' = ', np.mean(item)) 
    
# De volgende for-loop doet hetzelfde maar is wat omslachtiger    
for i in np.arange(len(data)):
    print('gemiddelde van  data[', i, ']  = ', np.mean(data[i]))
 
matrix = np.array(data) # .. verder oefenen met numpy-array matrix
print('\n matrix = ', matrix) # stiekem \n toegevoegd (het newline symbool)

for rij in matrix: # rij is de naam van een variabele; betekenisvol gekozen!
    print('gemiddelde van ', rij, ' = ', np.mean(rij))

# Berekeningen hieronder lukken alleen met NumPy arrays:
dim = np.shape(matrix)   # Merk op: dim is een tuple, zie de Variable Explorer
for i in np.arange(dim[1]):
    print('gemiddelde van kolom ', i, ' = ', np.mean(matrix[:,i]))

# Als je data eenmaal in een matrix staan heb je geen for-loops nodig:     
print('Kolom gemiddeldes = ', np.mean(matrix, axis=0))
print('Rij   gemiddeldes = ', np.mean(matrix, axis=1))

#%%
#3.5.1 Oefenopdracht: Gebruik van maskers

## Dit script demonstreert het gebruik van maskers
## in selectie van data. In dit geval de resultaten van een tentamen.

# Lijsten/arrays zelf invullen svp
naam = np.array(["Merel","David","Birte","Anne","Lieve"]) # naam: Bevat naam van studenten
stno = np.array([365, 466, 564, 769, 863]) # stno: Bevat studentnummer studenten.
opg1 = np.array([5,6,4,7,8]) # opg1: punten voor opgave 1 etc.
opg2 = np.array([10,3,8,6,5])
opg3 = np.array([5,8,3,10,10])

## Alle arrays zijn 1-dimensionaal en op dezelfde manier georderd.
## Voor dit tentamen waren 3*10 punten te verdienen. Met 6 gemiddeld
## punten heeft de kandidaat een voldoende.
points = np.mean([opg1, opg2, opg3], axis=0)

vol_masker = points >= 6  # vol staat voor voldoende
 

# Nu kan selectie plaatsvinden
vol_naam = naam[vol_masker]
vol_stno = stno[vol_masker]
vol_cijfer = points[vol_masker]

print("Studenten met een voldoende:")
for it in range (len(vol_naam)):
	print("%s (studnr %s ) heeft %s punten" % (vol_naam[it], vol_stno[it], vol_cijfer[it]))


#x = np.logical_and(opg1>=6,opg2>=6)
#print(x)
#for i in range (len(x)):
    #if x[i]:
        #if opg3[i] >= 6:
            #print(naam[i])

y = np.logical_and(opg1>=6,np.logical_and(opg2>= 6,opg3>=6)) 
print(y)    
Ijverig = naam[y]  
print(Ijverig)  

#ijv_masker = [True,True,True,True,True] 
#opgaves = [opg1, opg2, opg3]
#for it in range(len(naam)):
    #for opgave in opgaves:
        #if opgave[it] < 6:
            #ijv_masker[it] = False
            #break

#ijv_naam = naam[ijv_masker]

#print("Ijverige studenten:", ijv_naam)         
#%%
## Het volgende script demonstreert een aantal veel-
## gebruikte kansverdelingen en het seeden van de random
## number generator.

# Seed de RNG met 43890
x = np.random.seed(43890)
print(x)
## Random getallen uit een aantal verdelingen.
# Uniform [0,1)
unif     = np.random.random()
print(unif)

# Normaalverdeeld gem. = mu, std. = sigma
mu = 9
sigma = 2
normaalv = np.random.normal(mu,sigma)
print(normaalv)

# Poisson verdeeld, lambda = lamb
lamb = 5
poissonv = np.random.poisson(lamb)
print(poissonv)

## Om meerdere samples te nemen, werkt op elke verdeling
normv10x10 = np.random.normal(mu,sigma,size=[10,10])       
print(normv10x10)   

#%%
#3.6.1 Oefenopdracht: random getallen en pi
lijst = []

x = np.random.random(size=5000)
y = np.random.random(size=5000) 
r = (x**2 + y**2)**0.5
print(r)

for i in r:
    if i<1:
        lijst.append(1)
    else:
        lijst.append(0)
print(lijst)

gemiddelde = np.mean(lijst)
pi = gemiddelde*4
print(pi)

y2 = np.pi - pi

#%%
N = []
delta_pis = []
temp_pis = []
temp_N = []
seeds = [123456, 87654, 3456, 123987, 45676789]
for seed in seeds:
    temp_pis = []
    temp_N = []
    np.random.seed(seed)
    for size in range(3, 9):
        x = np.random.random(size=10**size)
        y = np.random.random(size=10**size)
        r = (x**2 + y**2)**0.5
        in_cirkel = r < 1
        pi = np.mean(in_cirkel)*4
        delta_pi = abs(np.pi - pi)
        temp_N.append(10**size)
        temp_pis.append(delta_pi)
    N.append(temp_N)
    delta_pis.append(temp_pis)
for i in range(len(N)):
    plt.loglog(N[i], delta_pis[i])
plt.show()
    