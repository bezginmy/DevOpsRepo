class Student:
 name=str
 exam_max=float
 lab_max=float
 lab_num=int
 k=float
 labs=list()
 exam=float
 def __init__(self, name_arg, conf):
  self.name=name_arg
  self.exam_max=conf['exam_max']
  self.lab_max=conf['lab_max']
  self.lab_num=conf['lab_num']
  self.k=conf['k']
  print('New student created: ', self.name, self.exam_max, self.lab_max, self.lab_num, self.k, sep=' ')
  self.labs=[0]*self.lab_num
  self.exam=0
 
 def make_lab(self,*mn):
  if (len(mn)==1):
   m=mn[0]
   for i in range(len(self.labs)):
    if float(self.labs[i])==0:
     self.labs[i]=m
#     print('zero mark found')
#     print(self.labs)
     break 
  if (len(mn)==2):
   m=mn[0]
   n=int(mn[1])
   if(n<self.lab_num):
    if (m<self.lab_max):
     self.labs[n]=m
    else:
     self.labs[n]=self.lab_max
  return self

 def make_exam(self,m):
  if(m<self.exam_max):
   self.xam=m
  else:
   self.exam=self.exam_max
  return self

 def is_certified(self):
  sum=float(self.exam)
  for lab in self.labs:
   sum+=lab
  if (sum/(self.lab_num*self.lab_max+self.exam)<self.k):
   return (sum, False)
  else:
   return (sum, True)

oleg=Student('Oleg', {'exam_max':30, 'lab_max':7, 'lab_num':10, 'k':0.61})
oleg.make_lab(1)
print ('Labs: ', oleg.labs,',exam: ', oleg.exam, sep=' ') 
oleg.make_lab(8,0)
print ('Labs: ', oleg.labs,',exam: ', oleg.exam, sep=' ')
oleg.make_lab(1)
print ('Labs: ', oleg.labs,',exam: ', oleg.exam, sep=' ')
oleg.make_lab(10,7)
print ('Labs: ', oleg.labs,',exam: ', oleg.exam, sep=' ')
oleg.make_lab(4,1)
print ('Labs: ', oleg.labs,',exam: ', oleg.exam, sep=' ')
oleg.make_lab(5)
print ('Labs: ', oleg.labs,',exam: ', oleg.exam, sep=' ')
oleg.make_lab(6.5)
print ('Labs: ', oleg.labs,',exam: ', oleg.exam, sep=' ')
oleg.make_exam(32)
print ('Labs: ', oleg.labs,',exam: ', oleg.exam, sep=' ')
  
print (oleg.is_certified())

oleg.make_lab(7,1)
print ('Labs: ', oleg.labs,',exam: ', oleg.exam, sep=' ')
  
print (oleg.is_certified())

