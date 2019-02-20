import numpy as np
from operator import itemgetter

dic = []
data = np.loadtxt('finefoods.txt',dtype = str,delimiter = '\n')


	##user_list = []
temp = [None] * 4 ##record transformation [productID,helpfulness,score,time]
user = ""         ##userID
boo = 0           ##if it is '1' then it's a new user
index = None
for line in data:
	if line[0:9] == "product/p":
		#print (temp)
		if len(user) != 0:
			for record in dic:
				if record[0] == user:
					record+=[temp]
					boo = 1
			if boo == 0:
				dic.append([user,temp])
			temp = [None] * 4
			temp[0] = line[19:]
	elif line[0:9] == "review/us":
		user = line[15:]
	        '''
		if user not in user_list:
			boo = 1
		else:
			boo = 0
		'''

	elif line[0:9] == "review/he":
		temp[1] = line[20:]
	elif line[0:9] == "review/sc":
		temp[2] = line[14:]
	elif line[0:9] == "review/ti":
		temp[3] = line[13:]


import pickle

purchase_few = []
purchase_5 = []
purchase_10 = []
purchase_20 = []
purchase_30 = []
purchase_40 = []



for line in dic:
    if len(line) >= 41:
        purchase_40.append(line)
    elif len(line) >= 31:
        purchase_30.append(line)
    elif len(line) >= 21:
        purchase_20.append(line)
    elif len(line) >= 11:
        purchase_10.append(line)
    elif len(line) >= 6:
        purchase_5.append(line)
    else:
        purchase_few.append(line)

with open('user_purchase40up.pkl',"wb") as p40up:
    pickle.dump(purchase_40, p40up)

with open('user_purchase30up.pkl',"wb") as p30up:
    pickle.dump(purchase_30, p30up)

with open('user_purchase20up.pkl',"wb") as p20up:
    pickle.dump(purchase_20, p20up)

with open('user_purchase10up.pkl',"wb") as p10up:
    pickle.dump(purchase_10, p10up)

with open('user_purchase5up.pkl',"wb") as p5up:
    pickle.dump(purchase_5, p5up)

with open('user_purchasefew.pkl',"wb") as pfew:
    pickle.dump(purchase_few, pfew)




data = []
