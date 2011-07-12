#!/usr/bin/python
from tools import *
import math

def getweight(x, wordfreq, normalize = 0):
	step = 5
	if normalize:
		if len(x) <= 1:
			step = 1.0
		else:
			step = 1.0 / (len(x) - 1)
	tmp = map(lambda y:(y,getwordfreq(wordfreq, y)), x)
	tmp.sort(lambda a,b: a[1]-b[1])
	tmpdict = {}
	tmpindex = -1
	tmpvalue = -1
	for a in range(len(tmp)):
		if tmpvalue != tmp[a][1]:
			tmpindex = a
		tmpdict[tmp[a][0]] = step * tmpindex
	return map(lambda y: (y, tmpdict[y]), x)

def getverticle(sentencelist, wordfreq):
	weightedsentencelist = map(lambda x: getweight(x, wordfreq, 1), sentencelist)
	result = {}
	resultdivide = {}
	for sentence in weightedsentencelist:
		for k, v in sentence:
			if k in result:
				result[k] += v
				resultdivide[k] += 1
			else:
				result[k] = v
				resultdivide[k] = 1
	for k, v in result.items():
		result[k] = v / resultdivide[k] #getwordfreq(wordfreq, k)
	return result

if __name__ == '__main__':
	import nlphtml
	rawtext=loadrawtextfile('test_data/xx.txt')
	wordlist = getwordlist(rawtext)
	wordfreq = countwords(wordlist,1);
	sentencelist = getsentencelist(rawtext)
	weightedsentencelist = map(lambda x: getweight(x, wordfreq), sentencelist)
	sb = nlphtml.htmlstep()
	for x in weightedsentencelist[:500]:
		sb.addsentence(x)
	print sb.out()

