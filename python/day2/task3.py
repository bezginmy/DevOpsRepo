import sys
s=str(sys.argv[1])
i=int(0)
ctr=int(0)
result=True
while(i<len(s)):
 if (s[i]=='('):
  ctr=ctr+1
 if (s[i]==')'):
  ctr=ctr-1
 if (ctr<0):
  result=False
 i+=1
if (ctr!=0):
 result=False
if (result==False):
 print("Brackets not OK")
else:
 print("Brackets OK")
