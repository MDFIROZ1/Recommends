import numpy as np

data = np.loadtxt('edge.txt', dtype = str, delimiter = '\n')
countedge = []
for edge in data:
    edge  = edge.split()
    boo = 0
    for exis in countedge:
        if edge[0] == exis[0] and edge[1] == exis[1]:
            exis[2] += 1
            boo = 1
        if boo == 0:
            edge.append(1)
            countedge.append(edge)


text_file = open("countedge.txt", "w")
for edge in countedge:
    text_file.write(edge[0])
    text_file.write(' ')
    text_file.write(edge[1])
    text_file.write(' ')
    text_file.write(edge[2])
    text_file.write('\n')
text_file.close()
