import numpy as np
def walsh(data1,data2):
  data1=np.array(data1).flatten()
  data2=np.array(data2).flatten()
  xoredarr=[]
   #entropy source chaotic s-box    -->  data1 
   #shuffled s-box                  -->  data2   
  sumarr=[]
  for i in range(0,256):
    sum=0;
    for j in range(0,256):
      xored=0
      data1bin=format(data1[j],'b').zfill(8)
      wbin=format(i,'b').zfill(8)
      for k in range(0,8):
        xored=xored^(int(data1bin[k])*int(wbin[k]))
      xoredarr.append(xored)
      xored=xored^data2[j]
      xored=pow(-1,abs(xored))
      sum=sum+xored
    sumarr.append(sum)
  return max(sumarr)