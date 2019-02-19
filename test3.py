import numpy as np
from operator import itemgetter


data = np.loadtxt("finefoods.txt.partab",dtype = str,delimiter = '\n')

dic = []
user_list = []
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

########sort the purchase record by time#####################

for rec in dic:
	rec[1:len(rec)] = sorted(rec[1:len(rec)],key = itemgetter(3))

#######build the edge######################
text_file = open("edge.txt", "w")
prod_a = None
prod_b = None
for rec in dic:
	if len(rec) > 2:
		for ele in range(1,len(rec)-1):
			text_file.write(rec[ele][0])
			text_file.write(' ')
			text_file.write(rec[ele+1][0])
			text_file.write('\n')

text_file.close()

		




'''
text_file = open("Outputtest.txt", "w")
for u in dic:
	text_file.writelines(u)

text_file.close()
'''
