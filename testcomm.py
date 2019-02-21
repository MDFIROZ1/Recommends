import pickle
from collections import  Counter 
with open('labelcurr.pkl',"rb") as train:
    data = pickle.load(train)

print len(data)
'''
uni = set()
for i in data:
    uni.add(i)
print len(uni)


for i in data:
    print i
print data
'''
data = Counter(data)
print len( data.most_common(10000))

print len(set(data))
print len(data)
