import csv

for i in xrange(339):
	with open("vote #%d.csv" %(i+1), 'r') as file:
		with open("vote%d.csv" %(i+1), 'w') as newFile:
			file.next() # skip header line
			for line in file:
				newFile.write(line)

