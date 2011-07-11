import re
from tokenize import *

def countwords(x, weight = 1.0):
	result = {}
	for k in x:
		if k in result:
			result[k] += weight
		else:
			result[k] = weight
	return result

def preserve_countwords(x, result, weight = 1.0):
	for k in x:
		if k in result:
			result[k] += weight
		else:
			result[k] = weight

def countandsort(x):
	result = countwords(x).items()
	result.sort(lambda x,y:y[1]-x[1])
	return result

def generatepair(x, t):
	if len(x) - t < 1:
		return []
	return map(lambda a: ' '.join(a), zip(x[:-t], x[t:]))

def generatereversedpair(x, t):
	if len(x) - t < 1:
		return []
	return map(lambda a: ' '.join(a), zip(x[t:], x[:-t]))

def generatengram(x, n):
	if len(x) < n:
		return []
	if n == 1:
		return x
	result = []
	for a in range(len(x)-n+1):
		result.append(x[a:a+n])
	return result

def comparefloat(a,b):
	if a > b:
		return 1
	elif a == b:
		return 0
	else:
		return -1

def filtersingle(x, n):
	return filter(lambda a: a[1] > n, x)

def printpairs(x):
	for a in x:
		print a[0] + '\t=>\t' + a[1].__str__()

def ppppp():
	print '=' * 30

def loadrawtextfile(filename):
	"""
	This function replace all numbers to nn and strip all "|" 
	"""
	return stripnumber(open(filename,'r').read().strip().lower().replace('|',' '))

def splitpairwithvalue(pairlist):
	"""
	[['a|b',5.5], ...] -> {'a':{'b':5.5, ...}, ...}
	"""
	result = {}
	for a in pairlist:
		tmp = a[0].split(' ')
		if tmp[0] in result:
			result[tmp[0]][tmp[1]] = a[1]
		else:
			result[tmp[0]] = {tmp[1]:a[1]}
	return result

###################################################
#
# The following three functions are for intimacy.
#
###################################################

def addpairwithvalue(sentence, step, value, result):
	"""
	@sentence: 	[a,b,c,d]
	@step: 		offset between two words
	@value: 	the weight
	@result: 	the final dict
	"""
	for index in xrange(len(sentence) - step):
		word1 = sentence[index]
		word2 = sentence[index+step]
		if not (word1 in result):
			result[word1] = {}
		if not(word2 in result[word1]):
			result[word1][word2] = value
		else:
			result[word1][word2] += value

def addreversedpairwithvalue(sentence, step, value, result):
	"""
	@sentence: 	[a,b,c,d]
	@step: 		offset between two words
	@value: 	the weight
	@result: 	the final dict
	"""
	for index in xrange(len(sentence) - step):
		word2 = sentence[index]
		word1 = sentence[index+step]
		if not (word1 in result):
			result[word1] = {}
		if not(word2 in result[word1]):
			result[word1][word2] = value
		else:
			result[word1][word2] += value

def getpairwithprobability(result, wordfreq):
	for k, tmp in result.items():
		factor = 1.0 / getwordfreq(wordfreq, k)
		for kk, vv in tmp.items():
			result[k][kk] = vv * factor

def getwordfreq(wordfreq, key):
	return wordfreq[key] if key in wordfreq else 1

def writetofile(filename, txt):
	tmp = open(filename, 'w')
	tmp.write(txt)
	tmp.close()

def loadandeval(filename):
	tmp = open(filename, 'r')
	txt = tmp.read()
	tmp.close()
	return eval(txt)

valuedesc = lambda x,y:y[1]-x[1]

def printdict(d):
	for k,v in d.items():
		print k, '->', v

def gettopitems(wordlist, rate):
	"""
	wordlist: sorted [[word, freq], ...]
	rate: a float number [0.0 ... 1.0]
	"""
	tmp = map(lambda x: x[1], wordlist)
	total = sum(tmp)
	if total == 0:
		return []
	tmpint = int(total * rate)
	offset = 0
	checkit = 0
	while checkit < tmpint:
		checkit += tmp[offset]
		offset += 1
	return wordlist[:offset]
