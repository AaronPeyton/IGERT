import csv
file_names = []
for i in xrange(1,339):
	file_names.append("vote%d.csv" %(i+1))

sen_dict = {}
with open("vote1.csv", "rb") as v1:
	reader = csv.DictReader(v1)	
	for row in reader:
		sen_dict[row["name"]] = [row["vote"]]

for f_name in file_names:
	with open(f_name, 'rb') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			sen_dict[row["name"]].append(row["vote"])
lst = ['']
for bill in range(1, 340):
	lst.append('Bill %d' %bill)

with open("final.csv", "wb") as final:
	writer = csv.writer(final)
	writer.writerow(lst)
	for name, vote in sen_dict.iteritems():
		temp = [name]
		for vote_Num in xrange(339):
			temp.append(sen_dict[name][vote_Num])
		writer.writerow(temp)
