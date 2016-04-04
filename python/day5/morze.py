def encode_morze(text)
 alphabet='abcdefghijklmnopqrstuvwxyz1234567890'
 morzecode=['.-','-...', '-.-.', '-..', '.', ']
 diagram=''
 for i in range(len(text)):
  pos=alphabet.find(text[i])
  if pos>=0:
   for j in range(len(morzecode[pos])):
    if morzecode[pos][j]=='.':
     diagram=diagram+'^'
    if morzecode[pos][j]=='-':
     diagram=diagram+'^^^'
    if (j<len(morzecode[pos])-1):
     diagram=diagram+' '
   if (i<(len(text)-1):
    diagram=diagram+(' ')*3
  elif(text[i]==' '):
   diagram=diagram+(' ')*7
 return diagram

  
