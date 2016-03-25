import sys
key = str("aaaaabbbbbabbbaabbababbaaababaab")
alphabet = str("abcdefghijklmnopqrstuvwxyz")
TemplatePhrase = str ("You and I just have a dream to find our love a place where we can hide away")
cypher1 = str("")
cypher2 = str("")
plainstr = str (sys.argv[1])
for i in range (0, len(plainstr)):
 pos = int(alphabet.find(plainstr.lower()[i]))
 cypher1 = cypher1 + key[pos:pos+5]

j=int (0)
for i in range (0, len(TemplatePhrase)):
 if (i >= len(cypher1)):
  break 
 if (j>=len(TemplatePhrase)):
  print ("ERROR: not sufficient template phrase length")
  break
 while (TemplatePhrase[j]==' '):
   cypher2 = cypher2 + TemplatePhrase[j]
   j+=1
 if (cypher1[i]=='a'):
  cypher2 = cypher2 + TemplatePhrase.lower()[j]
 if (cypher1[i]=='b'):
  cypher2 = cypher2 + TemplatePhrase.upper()[j] 
 j+=1

print (cypher2)
