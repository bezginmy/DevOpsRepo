def count_holes(n):
 digits='0123456789-+'
 holecount=[1,0,0,0,1,0,1,0,2,1]
 nstr=''
 if (type(n)==int):
  if (n>=0):
   nstr=str(n)
  else:
   nstr=str((-1)*n)
 elif (type(n)==str):
  for i in range(len(n)):
   if ((0<=digits.find(n[i])<10) or ((digits.find(n[i])>=10) and (i==0))): 
    if ((len(nstr)>0) or (0<digits.find(n[i])<10) or ((i==len(n)-1) and (digits.find(n[i])<10))):
     nstr=nstr+n[i]
   else:
    return 'ERROR'
 else:
  return 'ERROR'
 if (len(nstr)==0):
  return 'ERROR'
 else:
#  print (nstr)
  result=int(0)
  for i in range(len(nstr)):
   result+=holecount[int(nstr[i])]
  return result

print(count_holes(906))
