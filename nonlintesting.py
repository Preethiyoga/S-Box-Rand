import originalSbox
import rowshuff
import rowcolshuff
import colshuff
import math
import nonlinearity
import numpy as np
import pandas as pd


sbox100=[]
for i in range(0,100):
    sbox100.append(originalSbox.generateAES().tolist())

def nonlinrowcol():
    min1lis=[]
    max1lis=[]
    avg1lis=[]
    for i in range(0,32):
        min1=math.inf
        max1=0
        sum1=0
        for j in range(0,100):
            shuffled = rowcolshuff.getRowColShuffled(i,sbox100[j])
            min1=min(min1,128-0.5*(nonlinearity.walsh(sbox100[j],shuffled)))
            max1=max(max1,128-0.5*(nonlinearity.walsh(sbox100[j],shuffled)))
            sum1+=128-0.5*(nonlinearity.walsh(sbox100[j],shuffled))
        avg1=float("{:.4f}".format((sum1/100)))
        min1lis.append(min1)
        max1lis.append(max1)
        avg1lis.append(avg1)
        print(min1,max1,avg1)
    df=pd.DataFrame.from_dict({'min':min1lis,'max':max1lis,'avg':avg1lis})
    df.to_excel('nonlinrowcol.xlsx',header=True,index=False)
    print("Addded!!!") 
        




def nonlinrow():
    min1lis=[]
    max1lis=[]
    avg1lis=[]
    for i in range(0,32):
        min1=math.inf
        max1=0
        sum1=0
        for j in range(0,100):
            shuffled = rowshuff.getRowShuffled(i,sbox100[j])
            min1=min(min1,128-0.5*(nonlinearity.walsh(sbox100[j],shuffled)))
            max1=max(max1,128-0.5*(nonlinearity.walsh(sbox100[j],shuffled)))
            sum1+=128-0.5*(nonlinearity.walsh(sbox100[j],shuffled))
        avg1=float("{:.4f}".format((sum1/100)))
        min1lis.append(min1)
        max1lis.append(max1)
        avg1lis.append(avg1)
        print(min1,max1,avg1)
    df=pd.DataFrame.from_dict({'min':min1lis,'max':max1lis,'avg':avg1lis})
    df.to_excel('nonlinrow1.xlsx',header=True,index=False)
    print("Addded!!!") 



def nonlincol():
    min1lis=[]
    max1lis=[]
    avg1lis=[]
    for i in range(0,32):
        min1=math.inf
        max1=0
        sum1=0
        for j in range(0,100):
            shuffled = colshuff.getColShuffled(i,sbox100[j])
            min1=min(min1,128-0.5*(nonlinearity.walsh(sbox100[j],shuffled)))
            max1=max(max1,128-0.5*(nonlinearity.walsh(sbox100[j],shuffled)))
            sum1+=128-0.5*(nonlinearity.walsh(sbox100[j],shuffled))
        avg1=float("{:.4f}".format((sum1/100)))
        min1lis.append(min1)
        max1lis.append(max1)
        avg1lis.append(avg1)
        print(min1,max1,avg1)
    df=pd.DataFrame.from_dict({'min':min1lis,'max':max1lis,'avg':avg1lis})
    df.to_excel('nonlincol.xlsx',header=True,index=False)
    print("Addded!!!") 
    print(min1,max1,avg1)


nonlinrowcol()