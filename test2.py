import numpy as np

data = np.loadtxt("finefoods.txt.partaa",dtype = str,delimiter = '\n')

dic = {}            
temp = [None] * 3 ##
user = ""
Boo = 0
for line in data:

	if line[0:9] = "product/p":
		temp[0] = line[19:] 
	elif line[0:9] = "review/us":
		user = line[15:]
		if user not in dic:
			
	

  
