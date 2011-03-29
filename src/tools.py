import re

cutter = re.compile(r"""[a-z0-9\-|']+""", re.I|re.U|re.M)
spliter = re.compile(r"""\.|!|\?|;""", re.I|re.U|re.M)
stripnumber_re = re.compile(r"""[0-9]+(\.[0-9]+)?""", re.I|re.U|re.M)

def stripnumber(str):
	return stripnumber_re.sub(' nn ', str)

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

def getwordlist(tmpstr):
	return cutter.findall(tmpstr)

def getsentencelist(tmpfile):
	return filter(lambda y:len(y)>0, map(lambda x: cutter.findall(x), spliter.split(tmpfile)))

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

valuedesc = lambda x,y:y[1]-x[1]

def printdict(d):
	for k,v in d.items():
		print k, '->', v
