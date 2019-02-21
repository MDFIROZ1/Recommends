import pickle
from operator import itemgetter
with open('prscore.pkl',"rb") as pronei:
    neighbor = pickle.load(pronei)


#count = 0
print neighbor['B00473TZY8']
#print len(neighbor)
#print len(neighbor[0])
#print len(neighbor[0][1])

#print neighbor[0]
#print len(neighbor[0])
'''
for  i in neighbor:
	if count <= 0:
		print i

		count +=1
		print i[1:len(i)-3]
	else:
		break
'''
diclist = []
for key, value in neighbor.items():
    temp = [key,value]
    diclist.append(temp)

diclist = sorted(diclist,key = itemgetter(1),reverse = True)

for i in range(10):
    print diclist[i]


