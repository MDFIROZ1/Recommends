import random
import pickle

with open('user_purchasefew.pkl',"rb") as train:
    data = pickle.load(train)

seq = list(range(len(data)))
a = random.sample(seq,len(data)//10*3)
'''
print len(data)
print data[0]
print len(a)
'''
test_data = []
for randnum in a:
    
    temp1 = []
    temp2 = []
    for ele1 in data[randnum][1:len(data[randnum])-3]:
	temp1.append(ele1[0])
    for ele2 in data[randnum][len(data[randnum])-3:]:
        temp2.append(ele2[0])
    test_data.append([temp1,temp2])


with open('testdatafew.pkl',"wb") as test:
    pickle.dump(test_data, test)

