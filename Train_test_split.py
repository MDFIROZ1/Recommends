import random
import pickle

with open('user_purchase10up.pkl',"rb") as train:
    data = pickle.load(train)

seq = list(range(len(data)))
a = random.sample(seq,len(data)//10*3)
print len(data)

test_data = []
temp = []
for randnum in a:
    temp = [data[randnum][1:len(data[randnum])-3], data[randnum][len(data[randnum])-3:]]
    test_data.append(temp)

print len(test_data)

with open('testdata.pkl',"wb") as test:
    pickle.dump(test_data, test)
