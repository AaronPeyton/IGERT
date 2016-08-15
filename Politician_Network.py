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
#print votes
			

#				Creating the Network graph

sen_Names = []
node_color = {}
for row in data:
	if row[0][-3:] == '[D]':
		node_color[row[0][5:-3]]='blue'
	elif row[0][-3:] == '[R]':
		node_color[row[0][5:-3]]='red'
	elif row[0][-3:] == '[I]':
		node_color[row[0][5:-3]]='yellow'
	sen_Names.append('%s' %row[0][5:-3])
 
sen_Names = sen_Names[1:]
#print sen_Names

g = nx.Graph()
gn = nx.Graph()
g.add_nodes_from(sen_Names)
gn.add_nodes_from(sen_Names)

for row in xrange(100):
	for col in xrange(row, 100):
		if row != col:
			g.add_edge(sen_Names[row], sen_Names[col], weight=abs(votes[row][col]-1000))
mst = nx.minimum_spanning_edges(g, data = True)
edgelist = list(mst)
gn.add_edges_from(edgelist)
#print sorted(edgelist)



labels={}
for name in sen_Names: 
	labels[name] = r'%s' %name
#print labels


positions = nx.spring_layout(gn, k = 0.40)
nx.draw_networkx_labels(gn, positions, labels, font_size = 11)
nx.draw(gn, positions,node_size = 55, node_color=node_color.values())

#								finding degree_centrality
centrality_dict = nx.degree_centrality(gn)
for k, v in centrality_dict.iteritems():
    print k,v


#								finding nx.shortest_path
s_path_dict = nx.shortest_path(gn) 
start = ''
end = ''
l_path = []
for key, mini_dict in s_path_dict.iteritems():
 	for k, v in mini_dict.iteritems():
 		if len(v) > len(l_path):
 			start = key
 			end = k
 			l_path = v
#print "start	: %s" %start
#print "end	: %s" %end
#print l_path


# start = ''
# end = ''
# l_path = []
# for key, mini_dict in s_path_dict.iteritems():
# 	for k, v in mini_dict.iteritems():
# 		if len(v) > len(l_path):
# 			start = key
# 			end = k
# 			l_path = v
# print "start	: %s" %start
# print "end	: %s" %end
# print l_path


#plt.savefig("Politician_Graph.png")
plt.show()
