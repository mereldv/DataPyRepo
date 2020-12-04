# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 09:55:23 2020

@author: merel
"""
import numpy as np

"""
#A
yeet = np.arange(1,11)
print(yeet)
uitkomst = yeet**yeet
print(uitkomst)
"""


"""
#B
mooie_lijst = np.arange(1.5,3.3,0.3)
print(mooie_lijst)
mooie_lijst2 = np.linspace(1.5,3.0,num=6)
print(mooie_lijst2)
"""


#C
yeet = np.arange(1,11)
uitkomst = yeet**yeet
gemiddelde = uitkomst.mean()
som = uitkomst.sum()
print(gemiddelde)
print(som)


#m = np.matrix(Z)
#print(m.max(), m.min())


""" 
a = [((0,0),(0.125, 0.25, 0.5,1)),
     ((0,1),(1,1.5,2)),
     ((1,0),(1,2,3,4)),
     ((1,1),(0.1,1,10)),
    ]     

for i in a:
    for j in i[1]:
        axarr[i[0][0],i[0][1]].plot(x,x**j)

f.suptitle("Vier plotjes tegelijk")
plt.show()
"""
# Korter
#f2 = [np.cos(ding)**2 if np.cos(ding) > 0 else np.cos(ding) for ding in x ]