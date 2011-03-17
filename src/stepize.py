from tools import *
import math
import nlphtml

rawfile=stripnumber(open('xx.txt','r').read().strip().lower().replace('|',' '))
wordlist = cutter.findall(rawfile)

### wordfreq is the count of each word ###
wordfreq = countwords(wordlist,1);

topword = wordfreq.items();
topword.sort(lambda x,y:y[1]-x[1]);
#rintpairs(topword[:50])
#ppppp()

curve = lambda x: 1.0/x

sentencelist = filter(lambda y:len(y)>0, map(lambda x: cutter.findall(x), spliter.split(rawfile)))
#print sentencelist[:10]
#ppppp()

def getweight(x, wordfreq):
	tmp = map(lambda y:(y,wordfreq[y]), x)
	tmp.sort(lambda a,b: b[1]-a[1])
	tmpdict = {}
	for a in range(len(tmp)):
		tmpdict[tmp[a][0]] = a*5
	return map(lambda y: (y, tmpdict[y]), x)

weightedsentencelist = map(lambda x: getweight(x, wordfreq), sentencelist)

sb = nlphtml.htmlstep()
for x in weightedsentencelist[:500]:
	sb.addsentence(x)

print sb.out()

exit()

#maxlen = max(map(lambda x: len(x), sentencelist))

result = {}
for cc in range(20, 0, -1):
	for x in sentencelist:
		preserve_countwords(generatepair(x, cc), result, math.exp(- ((cc-1)**2) /2))
	
pairfreq = filtersingle(result.items(),1)

# devided by the number of head(of the pair) to get the probability.
pairfreq = map(lambda x: (x[0], x[1] * 1.0 / wordfreq[x[0].split(' ')[0]]), pairfreq)
pairfreq.sort(lambda x,y:comparefloat(y[1],x[1]))
printpairs(pairfreq)
print ">>>" + cc.__str__()
ppppp()

