n=int(input("Please enter n: "))
rset=set(range(1, n+1))
excluded=set()
question=['No']
while (len(question)>0):
 question=str(input("Enter some set: ")).split()
 answer=""
 if (len(question)>1):
  answer=str(question[-1])
  question.pop(-1)
 for i in range(len(question)):
  question[i]=int(question[i])
 qset=set(question)
# print("question: ", qset, sep=" ")
 if(answer=="YES"):
  rset&=qset 
 if(answer=="NO"):
  rset-=qset
 print("result: ", rset, sep=" ")

#print("possible variants:", rset, sep=" ")


 
