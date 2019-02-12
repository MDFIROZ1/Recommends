import numpy as np

data = np.loadtxt("finefoods.txt.partaa",dtype = str,delimiter = '\n')

cnt = 0

for line in data:

	if cnt <= 100:
		if line[0:6] == 'produc':
			print line
		cnt +=1
	else:
		break

  
