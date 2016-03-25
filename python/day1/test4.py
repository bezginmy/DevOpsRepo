import sys
x=int(sys.argv[1])
fibo=int
pre=int
nex=int
fibo=0
nex=1
pre=0
if (x==0):
 fibo=0
if (x==1):
 fibo=1
while (x>1):
 x=x-1
 fibo=pre+nex
 pre=nex
 nex=fibo 
print fibo
