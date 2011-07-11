# coding=utf8
import re

# for cutting words.
cutter = re.compile(r"""[a-z0-9\-|,']+""", re.I|re.U|re.M)

# for spliting sentences.
spliter = re.compile(r"""\.|!|\?|;""", re.I|re.U|re.M)

# for replacing numbers with ' nn '.
#stripnumber_re = re.compile(r"""[0-9]+(\.[0-9]+)?""", re.I|re.U|re.M)
stripnumber_re = re.compile(r"""\d+(?:,\d+)*(\.[0-9]+)?""", re.I|re.U|re.M)

a_punctuations = [
		('’',"""'"""),
		('，',','),
		(',',' , '),
		("""'""",""" ' """)
		]

def stripnumber(tmpstr):
	return stripnumber_re.sub(' nn ', tmpstr)

def preprocessrawstr(tmpstr):
	# strip ambiguous punctuations.
	for tmpa, tmpb in a_punctuations:
		tmpstr = tmpstr.replace(tmpa, tmpb)

	# strip numbers.
	tmpstr = stripnumber(tmpstr)
	return tmpstr

def getwordlist(tmpstr):
	tmpstr = preprocessrawstr(tmpstr)
	return cutter.findall(tmpstr)

def getsentencelist(tmpstr):
	tmpstr = preprocessrawstr(tmpstr)
	# Remember, the invoking is not getwordlist, but cutter.findall.
	return filter(lambda y:len(y)>0, map(lambda x: cutter.findall(x), spliter.split(tmpstr)))

# for testing
if __name__ == '__main__':
	tmpstr = open('test_data/testnumber.txt', 'r').read()
	print getsentencelist(tmpstr)
