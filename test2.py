import numpy as np

data = np.loadtxt("finefoods.txt.partaa",dtype = str,delimiter = '\n')

dic = {}
temp = [None] * 4 ##record transformation
user = ""         ##userID
boo = 0           ##if it is new user
cnt = 0
for line in data:
	while cnt < 100:
	    cnt += 1
		if line[0:9] = "product/p":
			if boo = 1:
				dic[user] = [user,temp]
			else:
				dic[user] = dic[user]+[temp]

			temp = [None] * 4
			temp[0] = line[19:]
		elif line[0:9] = "review/us":
			user = line[15:]
			if user not in dic:
					boo = 1
		elif line[0:9] = "review/he":
			temp[1] = line[20:]
		elif line[0:9] = "review/sc"
			temp[2] = line[14:]
		elif line[0:9] = "review/ti"
			temp[3] = line[13:]

text_file = open("Outputtest.txt", "w")
for u in dic:
	text_file.write(dic[u])

text_file.close()
