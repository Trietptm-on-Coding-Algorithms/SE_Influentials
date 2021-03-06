import heapq
import csv
import operator

h = []

table = {}
excl = {}
exclude = open('exclusion.csv','r')
csvex = csv.reader(exclude,delimiter='\t')
for row in csvex:
	excl[row[0]] = 1

exclude1 = open('exclcomp.csv','r')
csvex1 = csv.reader(exclude1,delimiter='\t')
for row in csvex1:
	excl[row[0]] = 1


arr = ['following/ICSEconf.csv','following/icse2015.csv','following/icse2016.csv','following/ICSMConference.csv','following/esecfse.csv','following/ESEC2014.csv','following/ecoop2014.csv','following/ASEConf2014.csv','following/splashcon.csv','following/msrconf.csv','following/issta_conf.csv','following/ieee_re.csv','following/ModularityConf.csv','following/ObjectMgmtGroup.csv','following/vlhcc.csv','following/IEEEVISSOFT.csv']
f = open('following/top100.csv', "wb")
for i in range (len(arr)):
	fname = arr[i]
	sample = open(fname,'r')
	csv1 = csv.reader(sample,delimiter='\t')
	for row in csv1:
		if (excl.has_key(row[1]) or table.has_key(row[1])):
			x = 1	#doing timepass		
		else:
			table[row[1]] = 1	
			heapq.heappush(h,(-(int(row[3])),row[1]))
	sample.close()


for x in range(0,400):
	p = heapq.heappop(h)
	params = (p[1],-p[0])
	f.write('%s\t%s\n' % params)



f.close()
exclude.close()

