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
from operator import itemgetter
import random

#####label propagation############



with open('productneighbor.pkl',"rb") as pronei:
    neighbordic = pickle.load(pronei)

with open('prscore.pkl',"rb") as pr:
    prscore  = pickle.load(pr)

#######sort the product based on pagerank score###########
diclist = []

for key, value in prscore.items():
    temp = [key,value]
    diclist.append(temp)

diclist = sorted(diclist,key = itemgetter(1),reverse = True)

######adding user into a list based on the order of pagerank score#####
data2user_list = []
for rk in diclist:
    data2user_list.append(rk[0])
print data2user_list
#####creating each product's neighbor dictionary##############
result = collections.defaultdict(list)
for data in neighbordic:
    temp = []
    for nei in data[1:]:
	temp.append(nei[0])
    result[data[0]] = temp
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
	'''
        #print count.most_common()[0][0]
	most_common_list = count.most_common(10)
	if len(most_common_list) >=2:
	    if most_common_list[0][1] == most_common_list[1][1]:
	        for elem in range(1,len(most_common_list)-1):
		    if  most_common_list[elem][1] == most_common_list[elem+1][1]:	 
       		        continue
		    else:
		        rand = random.randint(0,elem+1)
		        labelcurr[index] = most_common_list[rand][0]

	else:
	'''
 	labelcurr[index] = count.most_common()[0][0]
    #print labelcurr
    #print labelbank
    print '*****'


#######output the commmunity############33
with open('labelcurr.pkl', 'wb') as out:
    pickle.dump(labelcurr, out)
with open('user_dic.pkl', 'wb') as out:
    pickle.dump(user_dic, out)
