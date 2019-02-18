import numpy as np

data = np.loadtxt("finefoods.txt.partaa",dtype = str,delimiter = '\n')

dic = []
user_list = []
temp = [None] * 4 ##record transformation [productID,helpfulness,score,time]
user = ""         ##userID
boo = 0           ##if it is '1' then it's a new user
cnt = 0
index = None
for line in data:
	while cnt < 100:
	        cnt += 1
		if line[0:9] == "product/p":
			if len(user) != 0:
				for record in dic:
					if record[0] == user:
						record+=[temp]
						boo = 1
				if boo == 0:
					dic.append([user,temp)

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

text_file = open("Outputtest.txt", "w")
for u in dic:
	text_file.writelines(u)

text_file.close()
