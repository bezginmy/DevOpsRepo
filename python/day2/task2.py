import sys
s=str(sys.argv[1])
wordbuffer=str('')
result=str('')
i=int(0)
while i<len(s):
 if(s[i]!=' '):
  wordbuffer=wordbuffer+s[i]
 else:
  result=s[i]+wordbuffer+result
  wordbuffer=''
 i+=1
 print(i, result)
result=wordbuffer+result
print(result)
