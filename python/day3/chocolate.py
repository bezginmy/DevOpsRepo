import sys
m = int(sys.argv[1])
n = int(sys.argv[2])
k = int(sys.argv[3])

for i in range(0,m-1):
 if ((i+1)*n==k):
  print("Vertical cut "+str(i+1)+": "+str(k)+" = "+str(i+1)+" x "+str(n))
for i in range(0,n-1): 
 if ((i+1)*m==k):
  print("Horizontal cut "+str(i+1)+": "+str(k)+" = "+str(i+1)+" x "+str(m))
