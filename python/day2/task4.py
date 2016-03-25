import sys
a1=int(sys.argv[1])
a2=int(sys.argv[2])
s=str
i=int(a1)
x1=int
x2=int
result=int(0)
while (i<=a2):
 s=str(i)
 if(len(s)<6):
  s='0'*(6-len(s))+s
# print(s)
 x1=int(s[0])+int(s[1])+int(s[2])
 x2=int(s[-1])+int(s[-2])+int(s[-3])
 if (x1==x2):
  result+=1
 i+=1
print(result)
