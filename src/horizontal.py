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
result_reversed = {}

for cc in range(10, 0, -1):
	for x in sentencelist:
		preserve_countwords(
				generatepair(x, cc),
				result,
				math.exp(- ((cc)**2) /2))
		preserve_countwords(
				generatereversedpair(x, cc),
				result_reversed,
				math.exp(- ((cc)**2) /2))

pairfreq = filtersingle(result.items(), 0)
pairfreq_reversed = filtersingle(result_reversed.items(), 0)

# devided by the number of head(of the pair) to get the probability.
print "step1"
pairfreq = 		map(lambda x: (x[0], x[1] * 1.0 / wordfreq[x[0].split(' ')[0]]), pairfreq)

print "step2"
pairfreq_reversed = 	map(lambda x: (x[0], x[1] * 1.0 / wordfreq[x[0].split(' ')[0]]), pairfreq_reversed)

# prefix p_ represents "probability".
print "step3"
p_forward = splitpairwithvalue(pairfreq)
print "step4"
p_backward = splitpairwithvalue(pairfreq_reversed)

word_horizon = []

print "step5"

method = 1

if method == 1:
	for word1, tmp in p_forward.items():
		p_total = 0
		for word2, p in tmp.items():
			if (word2 in p_backward) and (word1 in p_backward[word2]):
				p_total += p - p_backward[word2][word1]
		word_horizon.append((word1, p_total))
		print (word1, p_total)
elif method == 2:
	print p_forward.items()[:3]
	ppppp()
	print p_backward.items()[:3]
	ppppp()
	p_forward_item = map(lambda t: (t[0], sum(map(lambda m:m[1], t[1].items()))), p_forward.items())
	p_backward_item = dict(map(lambda t: (t[0], sum(map(lambda m:m[1], t[1].items()))), p_backward.items()))
	print p_forward_item[:20]
	print p_backward_item.items()[:20]
	for word1, p in p_forward_item:
		p_total = 0
		if word1 in p_backward_item:
			p_total = p - p_backward_item[word1]
		print (word1, 1 if p_total>0 else -1)

exit();

pairfreq.sort(lambda x,y:comparefloat(y[1],x[1]))
printpairs(pairfreq)
print ">>>" + cc.__str__()
ppppp()

