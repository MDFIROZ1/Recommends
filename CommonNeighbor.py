import pickle

with open('testdata.pkl',"rb") as test:
    testdata = pickle.load(test)


with open('productneighbor.pkl',"rb") as pronei:
    neighbordic = pickle.load(pronei)

totalguess = 0
correct = 0
wrong = 0

for data in testdata:
    totalguess += 1
    #######each data in testdata would be like
    #####[[purchase record in the past],[purchase record in the future]]
    #######count the score on the neighbor of purchase record######
    neighborscore = []
    for target in data[0]:
        for prod in neighbordic:
            if prod[0] == target:
                for neighbor in prod[1:]:
                    for existpair in neighborscore
                        if neighbor[0] in existpair[0]:
                            existpair[1] += neighbor[1]
                        else:
                            neighborscore.append(neighbor)

    ######sort the recommended score##########
    neighborscore = sorted(neighborscore,key = itemgetter(1))
    candidate = []
    for top3 in range(3):
        cand.append(neighborscore.pop())
    ######counting the performance##################
    boo = 0
    for top3 in candidate:
        for answer in data[1]:
            if top3 == answer:
                boo = 1
                correct += 1
    if boo == 0:
        wrong += 1

text_file = open("result.txt", "w")
text_file.write('Total guess: %s' % str(totalguess))
text_file.write('Correct answer: %s' % str(correct))
text_file.write('Wrong answer: %s' % str(wrong))
text_file.write('Correctness: %s' % str(correct/totalguess))
