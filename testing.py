import originalSbox
import rowshuff
import rowcolshuff
import colshuff
import math
import sac
import nonlinearity
import pandas as pd
sbox100=[]
for i in range(0,100):
    sbox100.append(originalSbox.generateAES().tolist())



def sacrow():
    min1lis=[]
    max1lis=[]
    avg1lis=[]
    for i in range(0,32):
        min1=math.inf
        max1=0
        sum1=0
        
        for j in range(0,100):
            temp = rowshuff.getRowShuffled(i,sbox100[j])
            min1=min(float(min1),sac.SAC(temp))
            max1=max(float(max1),sac.SAC(temp))
            sum1+=sac.SAC(temp)
        avg1=float("{:.4f}".format((sum1/100)))
        min1lis.append(min1)
        max1lis.append(max1)
        avg1lis.append(avg1)
        # print(min1lis)
        # print(min1,max1,avg1)
    df=pd.DataFrame.from_dict({'min':min1lis,'max':max1lis,'avg':avg1lis})
    df.to_excel('sacrow.xlsx',header=True,index=False)
    print("Addded!!!")    


    

def sacrowcol():
    min2lis=[]
    max2lis=[]
    avg2lis=[]
    for i in range(0,32):

        min2=math.inf
        max2=0
        sum2=0
        for j in range(0,100):
            temp = rowcolshuff.getRowColShuffled(i,sbox100[j])
            min2=min(float(min2),sac.SAC(temp))
            max2=max(float(max2),sac.SAC(temp))
            sum2+=sac.SAC(temp)
        avg2=float("{:.4f}".format((sum2/100)))
        min2lis.append(min2)
        max2lis.append(max2)
        avg2lis.append(avg2)
        # print(min2,max2,avg2)
    df=pd.DataFrame.from_dict({'min':min2lis,'max':max2lis,'avg':avg2lis})
    df.to_excel('sacrowcol.xlsx',header=True,index=False)
    print("Addded!!!")    
    

    
def saccol():
    min3lis=[]
    max3lis=[]
    avg3lis=[]
    for i in range(0,32):
        min3=math.inf
        max3=0
        sum3=0
        for j in range(0,100):
            temp = colshuff.getColShuffled(i,sbox100[j])
            min3=min(float(min3),sac.SAC(temp))
            max3=max(float(max3),sac.SAC(temp))
            sum3+=sac.SAC(temp)
        avg3=float("{:.4f}".format((sum3/100)))
        min3lis.append(min3)
        max3lis.append(max3)
        avg3lis.append(avg3)
        # print(min3,max3,avg3)
    df=pd.DataFrame.from_dict({'min':min3lis,'max':max3lis,'avg':avg3lis})
    df.to_excel('saccol.xlsx',header=True,index=False)
    print("Addded!!!")




sacrow()
saccol()
sacrowcol()
