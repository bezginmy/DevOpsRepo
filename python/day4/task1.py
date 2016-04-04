def clean_list(in_list):
 res=[]
 for i in range(0,len(in_list)):
  isthere=bool(False)
  for j in range(0, len(res)):
   if (in_list[i]==res[j]):
    isthere=True
  if (not(isthere)):
   res.append(in_list[i])
 return res

import sys
x = [input() for i in range (0, int(input()))]
x1=clean_list(x)
print('[', end='')
for i in range(len(x1)):
 if(i<len(x1)-1):
  print (x1[i], end=' ')
 else:
  print (x1[i], end='')
print (']')  
