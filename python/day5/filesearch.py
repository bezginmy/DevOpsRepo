def file_search(folder, filename):
 if (type (folder)==str):
  if(folder==filename):
   return str(filename)
 if (type (folder)==list):
  if (folder[0]==filename):
   return str(folder[0])+'/'
  for i in range(1,len(folder)):
   subfolder=folder[i]
#   print('searching in '+str(subfolder)+' for name:'+str(filename))
   if (file_search(subfolder, filename)!=False):
    return str(folder[0])+'/'+str(file_search(subfolder, filename))
 return False


#print(file_search(['C:','backup.log','ideas.txt'], 'ideas.txt'))
print(file_search(['/home',['user1'],['user2',['my pictures'],['desktop','not this', 'and not this', ['new folder','hereiam.py']]],'work.ovpn', 'prometheus.7z', ['user3', ['temp'],],'hey.py'],'hereiam.py'))
#print(file_search(['D:',['recycle.bin'], ['tmp',['old'],['new folder1', 'asd.txt','asd.bak','find.me.bak']],'hey.py'], 'find.me.bak'))
