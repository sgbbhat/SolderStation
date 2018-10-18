import re
from collections import OrderedDict

fhandle = open("Intelis.txt", "r")
testDict = OrderedDict()
for line in fhandle:
	strline = str(line)
	strlinenew = re.sub(r'\s', '', strline)
	splitname = strlinenew.split(',')
	testDict[splitname[0]] = splitname[1:]

for key, val in testDict.items():
	print(key + " -> " + str(val))

for key in testDict.items():
	
