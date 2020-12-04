# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:53:37 2020

@author: merel
"""

import numpy as np
import matplotlib.pyplot as plt
#%%

x = np.linspace(-2*np.pi, 2*np.pi, num=1001)
y = np.sin(x)
plt.figure(figsize=[8,4])
plt.plot(x,y)
plt.savefig('sinus.png', format='png', dpi=300)
#%%
#OEFENOPDRACHT 1 

plt.figure(1) # begin met opbouwen van Figuur 1, default afmeting
 
x = np.linspace(-2*np.pi, 2*np.pi)
y = np.sin(x)
plt.plot(x, y, color = 'red')  # 1 curve is getekend

# nu een gladdere curve tekenen door meer (dan 50) punten te kiezen 
x = np.linspace(-2*np.pi, 2*np.pi, num=200)
y = np.sin(x)

# de breedte van de te tekenen curve moet ook worden aangepast
# anders zie je nog geen verschillen met de rode lijn
plt.plot(x, y, linewidth=0.1, color='black')

plt.savefig('sinus.png')      # sla verschillende bestandstypen 
plt.savefig('sinus.pdf')      # op om te kunnen vergelijken

plt.figure(2, figsize=[8,4])  # begin met opbouwen van Figuur 2
                              # met opgegeven afmeting in inches
plt.plot(x, np.cos(x))
plt.savefig('sinus')    # ... en weer een figuur opgeslagen.  
#%%
#VOORBEELD

plt.figure(1) # begin met opbouwen van Figuur 1, default afmeting
 
x = np.linspace(-2*np.pi, 2*np.pi)
y = np.sin(x)
plt.plot(x, y, color = 'red')  # 1 curve is getekend

# nu een gladdere curve tekenen door meer (dan 50) punten te kiezen 
x = np.linspace(-2*np.pi, 2*np.pi, num=200)
y = np.sin(x)

# de breedte van de te tekenen curve moet ook worden aangepast
# anders zie je nog geen verschillen met de rode lijn
plt.plot(x, y, linewidth=0.1, color='black')

plt.savefig('sinus.png')      # sla verschillende bestandstypen 
plt.savefig('sinus.pdf')      # op om te kunnen vergelijken

plt.figure(2, figsize=[8,4])  # begin met opbouwen van Figuur 2
                              # met opgegeven afmeting in inches
plt.plot(x, np.cos(x))
plt.savefig('cosinus.pdf')    # ... en weer een figuur opgeslagen.
#%%
#FORLOOPS VOORBEELD 
lijst = ["pa", "ma", 1, [2,3]]
print(lijst)
for elem in lijst:
    print(4*elem)

#%%
#4.2.1 Oefenopdracht: Spelen met lijsten en printen binnen for-loop
L1 = np.arange(0,100)

for elem in L1:
    L2 = 100*elem
    print(L2)

L3 = L2 - L1**2  
#print(L3)

L3_nieuw = np.sort(L3)
#print(L3_nieuw)
L4 = L3_nieuw[-9:][::-1]
#print(L4)
L5 = L4.reshape(3,3)
print(L5)

for elem in L5:
    print(elem)
#%%
#4.3.1 Oefenopdracht: Oefenen met het precies formatteren van tekst

t = np.pi
y = 22/7
print('Na',t,'seconden is de bal',y,'meter hoog'.format(t,y))
print('Na {:.2f} seconden is de bal {:.2f} meter hoog'.format(t,y))
#%%
"""  Data wegschrijven in een bestand inclusief een header
"""
# Specificeren van object in Python dat het nieuwe bestand aanwijst
# 'w' staat voor 'write' en geeft aan dat in het bestand geschreven mag worden 
file = open('vb1.txt', 'w')

# Aanmaken van numpy arrays om weg te schrijven naar bestand
x = np.linspace(-2*np.pi, 2*np.pi, num=20)
y = np.sin(x)

# Metadata
col0 =  '     i'  # een onbelangrijke string; alleen voor leesbaarheid
col1 =  '      x' # een onbelangrijke string; alleen voor leesbaarheid
col2 =  ' sin(x)' # een onbelangrijke string; alleen voor leesbaarheid
par1 = 50         # een waarde / parameter 1
par2 = 0.12       # een waarde / parameter 2

# Schrijven van header, herkenbaar aan # op eerste positie van elke regel
file.write('# Dit is de header (eerste regel) \n')
file.write('# Schaal parameter horizontaal:\t {:5.2f}\n'.format(par1))
file.write('# Schaal parameter verticaal  :\t {:5.2f}\n'.format(par2))
file.write('#{:s} \t {:s} \t {:s}\n'.format(col0, col1, col2))
# de opgegeven namen worden weggeschreven als een character-string met
# daartussen steeds een \t (tab) voorafgegaan/gevolgd door een spatie

# Schrijven van (meet)gegevens:
for i in range(len(x)):
   file.write('{:7d} \t {:7.4f} \t {:7.4f} \n'.format(i, x[i], y[i]))
# op iedere regel staat nu: een geheel getal op de eerste 7 posities, 
# spatie, tab, spatie, decimaal getal met 4 decimalen op 7 posities, 
# spatie, tab, spatie, decimaal getal met 4 decimalen op 7 posities,    
# spatie, en de regel wordt afgesloten met een \n (new-line symbool).
# MERK OP: de laatste  regel is een lege regel.
   
file.close()
#%%
#Oefenopdracht: Wegschrijven van data naar file


file = open('MijnEersteBestand.txt', 'w')
x = np.linspace(-1/2*np.pi,2*np.pi,num = 101)
y = np.sin(x)
z = np.cos(x)
t = y/z 

col0 ='x' 
col1 ='y'
col2 ='z' 
col3 ='t'

file.write('# Dit is de header \n')
file.write('#{:s} \t {:s} \t {:s} \t {:s}\n'.format(col0, col1, col2, col3))

for i in range(len(x)):
    file.write('{:.2f} \t {:.2f} \t {:.2f} \t {:.2f} \n'.format(x[i],y[i],z[i],t[i]))

file.close()
#%%
"""
Script om alle items in een bestand als string te interpreteren
Zo'n string bevat geen spaties of tab's.
Maak zelf je eigen oefen-bestand aan.
"""
f =  open("MijnEersteBestand.txt", "r")
block = f.readlines()

data = []   #  een lege Python lijst
for line in block:
    data.append( line.split())  
    print(data)
# check data na runnen script
#%%
'''
Voorbeeld: het gebruik van genfromtxt
'''
# de naam van het bestand
dir = 'http://nspracticum.science.uu.nl/DATA2020/DATA-Py/Databestanden/'
filename = dir+'vb1.txt'  # het 'optellen' van strings

# lees de data in dit tab-gescheiden bestand
data = np.genfromtxt(filename, delimiter='\t')
print(data)

# als het goed is kun je zien dat data een array met floats is
# en de size ervan is (20,3); zie in Spyder bij je Variable explorer
# of bekijk het resultaat van onderstaande print
print('size of data = ', np.shape(data)) 

# plot de ingelezen data; kolom 0 wordt niet gebruikt
(x, y) = (data[:,1], data[:,2])
plt.plot(x,y)

plt.show()
#%%
#4.5.1 Oefenopdracht: Importeren en bewerken

data = np.genfromtxt("Voorbeeld.txt", delimiter='\t')

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False 

f =  open("Voorbeeld.txt", "r")
block = f.readlines()

para = []
counthashtag = 0 
countgetallen = 0
for line in block:
  for elem in line:
      if elem[0] == '#':
          counthashtag += 1
          words = line.split(sep='\t')
          functie_aanroep = is_number(words[-1])
          if functie_aanroep == True:
              countgetallen += 1
              getal = float(words[-1])
              para.append(getal)
              
print("Er zijn",counthashtag,"commentaarregels gevonden")
print("Er zijn",countgetallen,"getallen gevonden")
print(para)
#%%


              

       
    



