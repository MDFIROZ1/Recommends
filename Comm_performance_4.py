import pickle
from collections import Counter

def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys[0]


with open('testdata40up.pkl',"rb") as test:
    testdata = pickle.load(test)

with open('labelcurr50it.pkl',"rb") as test:
    label = pickle.load(test)

with open('user_dic50it.pkl',"rb") as test:
    user_dic = pickle.load(test)

totalguess = 0
correct = 0
wrong = 0
'''
for data in testdata:
    totalguess += 1
    print totalguess
    recom = []
    for target in data[0]:
        for lab in label:
            if label[user_dic[target]] == lab and label.index(lab) != user_dic[target]:
                recom.append(getKeysByValue(user_dic, label.index(lab)))
    for ans in data[1]:
        if ans in recom:
            correct += 1
            break
    wrong += 1
'''
for data in testdata:
    totalguess += 1
    print totalguess
    recom = []
    labelcnt = []
    recomm_community = None
    for target in data[0]:
        labelcnt.append(label[user_dic[target]])
    count = Counter(labelcnt)
    recomm_community = count.most_common()[0][0]
    for lab in label:
        if lab == recomm_community:
            recom.append(getKeysByValue(user_dic, label.index(lab)))
    for ans in data[1]:
        if ans in recom:
            correct += 1
            break
    wrong += 1

text_file = open("result40up_Comm_50it.txt", "w")
text_file.write('Total guess: %s' % str(totalguess))
text_file.write('\n')
text_file.write('Correct answer: %s' % str(correct))
text_file.write('\n')
text_file.write('Wrong answer: %s' % str(wrong))
text_file.write('\n')
text_file.write('Correctness: %s' % str(float(correct)/float(totalguess)))
text_file.close()
