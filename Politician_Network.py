import csv
import networkx as nx
import matplotlib.pyplot as plt
#			Creating the adjacency matrix


data = list(csv.reader(open("Final_Inverted.csv")))

votes= [[0 for x in range(100)] for y in range(100)]

for row in xrange(1,100):
	for row2 in xrange(row+1,101):
		for col in xrange(1,340):
			if data[row][col] == data[row2][col]:
				votes[row-1][row2-1] += 1
				votes[row2-1][row-1] += 1
			else:
				votes[row-1][row2-1] -= 1
				votes[row2-1][row-1] -= 1

#print votes
"""
temp = 0
for col in xrange(1,340):
	if data[1][col] == data[1][col]:
		temp += 1
	else:
		temp -= 1
print temp
"""
			

#				Creating the Network graph

sen_Names = []
for row in data:
	sen_Names.append('%s' %row[0])
sen_Names = sen_Names[1:]
print sen_Names

g = nx.Graph()
g.add_nodes_from(sen_Names)
positions = nx.circular_layout(g)
#print positions

labels={}
for name in sen_Names: 
	labels[name] = r'%s' %name
#print labels

nx.draw_networkx_labels(g, positions, labels, font_size = 10)
nx.draw(g, positions)


plt.savefig("Politician_Graph.png")
plt.show()





















