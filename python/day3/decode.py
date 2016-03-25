import sys
key = str("aaaaabbbbbabbbaabbababbaaababaab")
alphabetLower = str("abcdefghijklmnopqrstuvwxyz")
alphabetUpper = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
cypher = str (sys.argv[1])
cypher1 = str("")
text = str("")
for i in range (0, len(cypher)):
 if(cypher[i]!=' '):
  if(alphabetLower.find(cypher[i])>=0):
   cypher1=cypher1+'a'
  if(alphabetUpper.find(cypher[i])>=0):
   cypher1=cypher1+'b'
i=int(0)
while(i+5<=len(cypher1)):
 pos=int(key.find(cypher1[i:i+5]))
 if (0 <= pos <= 26):
  text=text+alphabetLower[pos]
 else:
  print("invalid block:")
  print(i, cypher1[i:i+5])
  break
 i+=5

print(text)





















