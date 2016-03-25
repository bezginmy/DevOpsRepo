import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
z=int(sys.argv[3])
s=str
fin=str
if z==0:
   fin="."
else:
   fin="!"
if y==0:
   s="Everybody sing a song:"+fin
else: 
   s="Everybody sing a song:"+(y-1)*((((x-1)*("la"+"-")))+"la ")+((x-1)*("la"+"-")+"la"+fin)
print s
