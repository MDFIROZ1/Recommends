import networkx as nx
import pickle


with open('productneighbor.pkl',"rb") as pronei:
        neighbordic = pickle.load(pronei)



FG = nx.DiGraph()
alledge = []
for node in neighbordic:
	for ele in node[1:]:
		temp = [node[0],ele[0],ele[1]]
		alledge.append(tuple(temp))
		


FG.add_weighted_edges_from(alledge)

k =  nx.pagerank(FG)
print k

with open('prscore.pkl',"wb") as test:
    pickle.dump(k, test)
