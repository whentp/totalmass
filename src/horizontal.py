#!/usr/bin/python
from tools import *
import math
import nlphtml

rawtext=loadrawtextfile('test_data/xx.txt')
wordlist = getwordlist(rawtext)

### wordfreq is the count of each word ###
wordfreq = countwords(wordlist,1);

topword = wordfreq.items();
topword.sort(valuedesc);

curve = lambda x: 1.0/x

sentencelist = getsentencelist(rawtext)

def getweight(x, wordfreq):
	tmp = map(lambda y:(y,wordfreq[y]), x)
	tmp.sort(lambda a,b: b[1]-a[1])
	tmpdict = {}
	for a in range(len(tmp)):
		tmpdict[tmp[a][0]] = a*5
	return map(lambda y: (y, tmpdict[y]), x)

weightedsentencelist = map(lambda x: getweight(x, wordfreq), sentencelist)

result = {}
for cc in range(10, 0, -1):
	for x in sentencelist:
		preserve_countwords(generatepair(x, cc), result, math.exp(- ((cc)**2) /2))
	
pairfreq = filtersingle(result.items(),1)

# devided by the number of head(of the pair) to get the probability.
pairfreq = map(lambda x: (x[0], x[1] * 1.0 / wordfreq[x[0].split(' ')[0]]), pairfreq)
pairfreq.sort(lambda x,y:comparefloat(y[1],x[1]))
printpairs(pairfreq)
print ">>>" + cc.__str__()
ppppp()

