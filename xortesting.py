import originalSbox
import rowshuff
import rowcolshuff
import colshuff
import math
import xortest as xor
import numpy as np
import pandas as pd



sbox100=originalSbox.generateAES().tolist()
# for i in range(0,100):
#     sbox100.append(originalSbox.generateAES().tolist())



def nonlinrowcol():
    max1lis=[]
    for i in range(0,32):
        # for j in range(0,1):
        shuffled = rowcolshuff.getRowColShuffled(i,sbox100)
        # max1=xor.XORdist(sbox100[j])
        # print(xor.XORdist(sbox100[j]))
        max1lis.append(xor.XORdist(shuffled))
        print(max1lis)
    df=pd.DataFrame.from_dict({'maxIO_XOR':max1lis})
    df.to_excel('xorcolnew2.xlsx',header=True,index=False)
    print("Addded!!!") 
        


def nonlinrow():
    max1lis=[]
    for i in range(0,32):
        # for j in range(0,1):
        shuffled = rowshuff.getRowShuffled(i,sbox100)
        # max1=xor.XORdist(sbox100[j])
        # print(xor.XORdist(sbox100[j]))
        max1lis.append(xor.XORdist(shuffled))
        print(max1lis)
    df=pd.DataFrame.from_dict({'maxIO_XOR':max1lis})
    df.to_excel('xorrownew2.xlsx',header=True,index=False)
    print("Addded!!!") 
        



def nonlincol():
    max1lis=[]
    for i in range(0,32):
        # for j in range(0,1):
        shuffled = colshuff.getColShuffled(i,sbox100)
        # max1=xor.XORdist(sbox100[j])
        # print(xor.XORdist(sbox100[j]))
        max1lis.append(xor.XORdist(shuffled))
        print(max1lis)
    df=pd.DataFrame.from_dict({'maxIO_XOR':max1lis})
    df.to_excel('xorrowcolnew2.xlsx',header=True,index=False)
    print("Addded!!!") 
nonlinrow()