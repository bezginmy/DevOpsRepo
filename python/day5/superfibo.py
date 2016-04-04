def super_fibonacci(n,m):
 buffer=[1]*int(m)
 next=int
 if (n<=m):
  return 1
 else:
  for i in range(int(m),int(n)):
   next=0
   for j in range(0, m):
    next+=buffer[j]
   buffer[i%m-1]=next
#   print (buffer)
  return next

import sys
print (super_fibonacci(int(sys.argv[1]), int(sys.argv[2])))
