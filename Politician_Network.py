import csv
import networkx as nx
import matplotlib as plt
#			Creating the adjacency matrix


data = list(csv.reader(open("Final_Inverted.csv")))

sen_Names = []
for row in data:
	sen_Names.append(row[0])
#print sen_Names
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


