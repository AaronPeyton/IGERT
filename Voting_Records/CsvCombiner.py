import csv
file_names = []
for i in xrange(1,339):
	file_names.append("vote #%d.csv" %(i+1))

sen_dict = {}
with open("vote #1.csv", "rb") as v1:
	reader = csv.DictReader(v1)	
	for row in reader:
		print row["vote"]
		sen_dict[row["name"]] = sen_dict[row["vote"]]

for f_name in file_names:
	with open(f_name, 'rb') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			sen_dict[row["name"]].append(sen_dict[row["vote"]])

for bill, vote in sen_dict.iteritems():
	print bill
	print vote
