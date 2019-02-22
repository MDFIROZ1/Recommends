import pickle

with open('labelcurr.pkl',"rb") as pronei:
    neighbor = pickle.load(pronei)
with open('user_dic.pkl',"rb") as pronei:
    user = pickle.load(pronei)


#count = 0

print len(neighbor)
print user
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
