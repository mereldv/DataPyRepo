# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:01:41 2021

@author: merel
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m
import scipy.odr as odr

#2.1
data = np.genfromtxt("events_test_data.tsv", delimiter='\t')

treshhold = 150
filtered = []
for line in data:
    if (line[8]>treshhold or line[8] == -1) and (line[9]>treshhold or line[9] == -1) and (line[10]>treshhold or line[10] == -1) and (line[11]>treshhold or line[11] == -1):
        filtered.append(line)
print(filtered)

#2.2
integral1 = []
integral2 = []
integral3 = []
integral4 = [] 

for line in filtered:
    integral1.append(line[8])
    integral2.append(line[9])
    integral3.append(line[10])
    integral4.append(line[11])
    
binAmount = int(np.sqrt(len(filtered)))
plt.hist(integral1,bins = binAmount, range = [treshhold,15000],histtype='step', label = "Integral1")
plt.hist(integral2,bins = binAmount, range = [treshhold,15000],histtype='step', label = "Integral2")
#plt.hist(integral3,bins = binAmount, range = [treshhold,15000],histtype='step', label = "Integral3")
#plt.hist(integral4,bins = binAmount, range = [treshhold,15000],histtype='step', label = "Integral4")
plt.yscale("log")
plt.xlabel("Integral of the signal") 
plt.ylabel("Aantal waardes")
plt.legend(loc='upper right')
plt.title("Integral van detectors")
plt.xlim([0,15000])
plt.show()
plt.savefig("histogram%s.png" %treshhold)

def plotHist(dataset, bins = 100):
    plt.hist(dataset, bins, range = [0,15000], histtype='step')
    plt.yscale("log")
    plt.xlabel("Integral of the signal") 
    plt.ylabel("Aantal waardes")
    plt.title("Integral van detectors")
    plt.xlim([0,15000])
    plt.show()
    
plotHist(integral1, binAmount) 

def dataHist(dataset,valuefirstbin = treshhold, valuelastbin = 15000):
    binrange = np.linspace(valuefirstbin,valuelastbin, num=int(np.sqrt(len(dataset)))) 
    
    list1 = [] 
    
    for i in range(0,len(binrange)):
        if binrange[i] == binrange[-1]:  
            list1.append(binrange[-1])
        else:
            list1.append(binrange[i]+(0.5*(binrange[i+1]-binrange[i])))  #naar kijken

    events = [0] * (len(binrange)-1) 
    for i in dataset:
        for x in range(0,len(binrange)-1):
            if i > binrange[x] and i < binrange[x+1]:
                events[x] += 1
                
    events = np.array(events)
    list1 = np.array(list1)
    events = events.reshape(len(events),1)
    list1 = list1.reshape(len(list1), 1)
    y = np.concatenate((list1,events),axis=1)
    print(y) 
    return y

functie = dataHist(integral1)  

#2.3
def Exponential(x, A, x0):
    y = A * m.exp((-x)/x0)
    return y

#test = Exponential(1,1,1)
#print(test)

def Landau(x, A, c, mu):
    z = (x-mu)/c
    y = 1.64872*A*m.exp((z+m.exp(-z))*-0.5)
    return(y) 

#test = Landau(1,1,1,1)
#print(test)

def MuonFit(A, x):
    AL, cL, muL, AE, x0E = A
    return Landau(x, AL, cL, muL) + Exponential(x, AE, x0E)
#test = MuonFit([1,1,1,1,1],1)
#print(test)

odr_fit = odr.Model(MuonFit)
x = dataHist(integral1)[:,0]
y = dataHist(integral1)[:,1] 
sig_y = [] 
for i in range(0,len(dataHist(integral1, treshhold)[:,1])):
    sig_y.append(np.sqrt(dataHist(integral1, treshhold)[:,1][i]))
sig_y = np.array(sig_y)
odr_data  = odr.RealData(x,y,sy=sig_y)
odr_obj   = odr.ODR(odr_data,odr_fit,beta0 = [800,150,2000,400,2000])
odr_obj.set_job(fit_type=2)
odr_res   = odr_obj.run() 



    