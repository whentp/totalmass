#!/usr/bin/python
from tools import *
from horizontal import *

rawtext=loadrawtextfile('test_data/aaaaaa.txt')
sentencelist = getsentencelist(rawtext)

# result stores hashtable.
result = {}
for tmp in sentencelist:
	appendhorizontalposition_norepeat(tmp, result)

result = gethorizontalposition(result)
printdict(result)
