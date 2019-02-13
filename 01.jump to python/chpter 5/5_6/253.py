import pickle
f=open("hell.txt",'wb')
data={1:'yp',2:'ss'}
pickle.dump(data,f)
f.close()