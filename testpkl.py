import pickle

with open('productneighbor.pkl',"rb") as pronei:
    neighbor = pickle.load(pronei)


count = 0

print len(neighbor)
print len(neighbor[0][0])
print len(neighbor[0][1])

print neighbor[0]
'''
for  i in neighbor:
	if count <= 0:
		print i

		count +=1
		print i[1:len(i)-3]
	else:
		break
'''
