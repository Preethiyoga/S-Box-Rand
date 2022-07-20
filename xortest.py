import numpy as np

def XORdist(tempAES):
  fx=np.array(tempAES).flatten()
  xor=[]
  for i in range(1,256):
    for j in range(0,256):
      if(i!=j):
        xor.append(delta(fx,i,j))
  return (max(xor))

def delta(sbox,a,b):
  count=0
  for i in range(0,256):
    if (sbox[i]^sbox[i^a]==b):
      count+=1
  return count