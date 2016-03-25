import sys
s=str(sys.argv[1])
a=int(0)
b=int(len(s)-1)
result=True
while (a<=b):
 if s[a]==' ' or s[b]==' ':
  if s[a]==' ':
   a+=1
  if s[b]==' ':
   b-=1
 else:
  if s.lower()[a]!=s.lower()[b]:
   result=False
  a+=1
  b-=1
if result==True:
 print('YES')
else:
 print('NO')
