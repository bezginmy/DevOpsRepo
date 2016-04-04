languages=[[str(input('Please enter language '+str(i)+' ')) for i in range(int(input('Please enter number of languages for pupil ' +str(pupil)+' ')))] for pupil in range(int(input('Please enter number of pupils ')))]

alllang=set()
commonlang=set(languages[0])
langcount=dict()


for pupil in languages:
 alllang|=set(pupil)
 commonlang&=set(pupil)
 for language in pupil:
  if (language in langcount):
   langcount[language]+=1
  else:
   langcount[language]=int(1)

#int smallest=0
#str rarestlang=""
#for num in range(len(langcount:
#  if smallest<num:
#   smallest=num
#   rarestlang=langcount

print("All languages: ", alllang, sep=" ")
print("Common languages: ", commonlang, sep=" ")
print("Count of languages known: ", langcount, sep=" ")
