import numpy as np

data = np.loadtxt("finefoods.txt.partaa",dtype = str,delimiter = '\n')

cnt = 0

for line in data:
	print (line)
	
'''
	if cnt%8 == 2:
		if line[0:9] != "review/us":
			print line
	cnt +=1 	
'''
  
