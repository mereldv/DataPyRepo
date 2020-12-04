# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:35:30 2020

@author: merel
"""

import matplotlib.pyplot as plt
import numpy as np


# Begin met een subplots.
# f bevat de informatie van de gehele figuur.
# ax1 t/m ax3 bevatten informatie over de individuele plots.
# sharex en sharey zorgen ervoor dat zowel x- als y-as gedeeld zijn.
f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)

x = np.linspace(0,2*np.pi)
y = np.cos(x)**2
y2 = np.sin(x)**2
y3 = np.cos(x)*np.sin(x)
ax1.plot(x,y)
ax2.plot(x,y2)
ax3.plot(x,y3)

# Dit is finetuning. De eerste regel zet de ruimte tussen de figuren op 0.
# De tweede regel zet de markering langs de x-as uit voor alle plots behalve de laatste.
f.subplots_adjust(hspace=0)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible = False)

# Suptitle refereert naar de titel van de gehele figuur. Dit is dus een eigenschap van de totale figuur f.
f.suptitle("Drie plotjes tegelijk")
plt.plot()


"""
#Begin met een subplots.
#sharex ='col' zorgt dat de x-coordinaat gedeeld wordt over de kolommen
#sharey ='row' idem voor rijen en de y-coordinaat

f, axarr = plt.subplots(2, 2, sharex ='col', sharey ='row')

x = np.linspace(0,2*np.pi)

axarr[0,0].plot(x,np.cos(x)**2)                # linksboven
axarr[0,1].plot(x,np.sin(x)**2)                # rechtsboven
axarr[1,0].plot(x,np.cos(x)*np.sin(x))         # linksonder
axarr[1,1].plot(x,np.cos(x)**2*np.sin(x)**2)   # rechtsonder

#suptitle refereert naar de titel van de gehele figuur. Dit is dus een 
#eigenschap van de totale figuur f.
f.suptitle("Vier plotjes tegelijk")
plt.show()
"""