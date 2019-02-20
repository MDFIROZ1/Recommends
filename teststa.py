import numpy as np

data = np.loadtxt("edge.txt",dtype = str, delimiter = '\n')

for line in data:
	print len(line)
