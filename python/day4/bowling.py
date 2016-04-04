import sys
N=int(input("Enter number of targets:"))
K=int(input("Enter number of throws:"))
state=['I']*N
for i in range(0,K):
 x=str(input("Enter throw #"+str(i+1)+":"))
 x1=x.split(' ')
 l=int(x1[0])
 r=int(x1[1])
 for j in range (l-1, r):
  state[j]='.'
for i in state:
 print(i, end="")
print()
