# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 01:15:04 2016

@author: KID
"""
import collections
from collections import Counter
import numpy as np
import pandas as pd
import pickle

#####label propagation############

#file2 = pd.read_csv('bigger_twitter_data_2.csv')
file2 = pd.read_csv('bigger_twitter_data_2.csv', names = ['tweet_id','user_id','create_time','favorite_count','retweet_count','RT_user','RT_id','reply_user','reply_id','mention','text','log_index'])

file2.to_csv('reborn2.csv',columns = ['tweet_id','user_id','reply_id','RT_id'])
#print file2
data2user = []
A =  file2['user_id'] 
for i in range(0,len(A)):
    data2user.append(str(A[i]))

data2user_list = list(set(data2user))
data2user_list.sort
#print data2user_list

###############relation dictionary###############
want_set = set(data2user_list)
#print want_set
result = collections.defaultdict(list)
with open('wfw_test2.txt') as infile:
    for line in infile:
        line = line.strip().split(' ')
        
        if line[0] in want_set:
            result[line[0]] = [x for x in line[1:] if x in want_set]
#print result            
labelcurr = []
labelbank = []            
for i  in data2user_list:
    labelcurr.append([i])
    labelbank.append([i])

#print labelbank
#print labelcurr
#print '-----------------'
user_dic = dict()
i = 0
for element in data2user_list :
    user_dic[element] = i
    i= i +1

###propagate########    

######with relation_matrix######
""""    
k = 10 ##number of iteration
for iteration in range(0,k-1):
    for user in range(0,len(data2user_list)-1):
        for neighbor in range(0,len(data2user_list)-1):
            if relation_matrix[user][neighbor] ==1:
                labelbank[neighbor].append(labelcurr[user])
    for i in range(0,len(data2user_list)-1):
        most_common,num_most_common = Counter(labelbank[i]).most_common(1)[0]
        labelcurr[i] = most_common
"""
#####without relation_matrix######



k = 100 ##number of iteration
for iteration in range(0,k-1):
    print "iteration:"+str(iteration)
    if iteration == 0:
        for user in result:
            for neighbor in result[user]:
                labelbank[user_dic[neighbor]].append(labelcurr[user_dic[user]][0])
            #print neighbor
	    #print labelbank[user_dic[neighbor]]
	       # print labelcurr[user_dic[user]]
    else:
	for user in result:
            for neighbor in result[user]:
                labelbank[user_dic[neighbor]].append(labelcurr[user_dic[user]])
            #print neighbor
            #print labelbank[user_dic[neighbor]]
               # print labelcurr[user_dic[user]]

   
    for index,user_in_bank, in enumerate(labelbank):
        #print user_in_bank
        count = Counter(user_in_bank)
        #print count.most_common()[0][0]
        labelcurr[index] = count.most_common()[0][0]
   # print labelcurr
    #print labelbank
    print '*****'


#######output the commmunity############33
with open('labelcurr.pkl', 'wb') as out:
    pickle.dump(labelcurr, out)
with open('user_dic.pkl', 'wb') as out:
    pickle.dump(user_dic, out)
