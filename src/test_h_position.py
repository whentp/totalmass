#!/usr/bin/python
from tools import *
import math
import nlphtml
from horizontal import *

rawtext=loadrawtextfile('test_data/aaaaaa.txt')
wordlist = getwordlist(rawtext)

### wordfreq is the count of each word ###
wordfreq = countwords(wordlist,1);

topword = wordfreq.items();
topword.sort(valuedesc);

curve = lambda x: 1.0/x

sentencelist = getsentencelist(rawtext)

# result stores hashtable.
result = {}
i = 0
for tmp in sentencelist:
	appendhorizontalposition_norepeat(tmp, result)

print len(result.items())
result = gethorizontalposition(result)

printdict(result)
