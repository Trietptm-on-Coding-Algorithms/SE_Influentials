import csv
import operator

excl = {}

exclude = open('exclusion.csv','r')
csvex = csv.reader(exclude,delimiter='\t')
for row in csvex:
	excl[row[0]] = 1
	print row[0]
 

sample.close()
