import numpy as np
def SAC(tempAES):
  # a=1,10,100,1000,10000,100000,1000000,10000000
  fx=np.array(tempAES).flatten()
#   print(fx)
  count=0
  a=[1,2,4,8,16,32,64,128]
  for i in range(0,256):
    for j in range(0,8):
      binxored=bin((fx[i]^(fx[i^a[j]])))[2:]
      for i in range(0,len(binxored)):
        if(binxored[i]=='1'):
          count+=1
#"{:.2f}".format(float)
  return float("{:.4f}".format(float(count/(256*8*8))))


# def getSAC():
#   # a=1,10,100,1000,10000,100000,1000000,10000000
#   fx=rand()
#   print(fx)
#   count=0
#   a=[1,2,4,8,16,32,64,128]
#   for i in range(0,256):
#     for j in range(0,8):
#       binxored=bin((fx[i]^(fx[i^a[j]])))[2:]
#       for i in range(0,len(binxored)):
#         if(binxored[i]=='1'):
#           count+=1
# #"{:.2f}".format(float)
#   return "{:.4f}".format(float(count/(256*8*8)))

# SAC()