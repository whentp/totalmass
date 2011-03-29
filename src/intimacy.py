#!/usr/bin/python
from tools import *
import math

rawtext=loadrawtextfile('test_data/xx.txt')
wordlist = getwordlist(rawtext)

### wordfreq is the count of each word ###
wordfreq = countwords(wordlist,1);
sentencelist = getsentencelist(rawtext)

p_forward = {}
p_backward = {}

steps = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
for x in sentencelist:
	for cc in steps:
		addpairwithvalue(x, cc, math.exp(- ((cc)**2) / 2), p_forward)
		addreversedpairwithvalue(x, cc, math.exp(- ((cc)**2) / 2), p_backward)

getpairwithprobability(p_forward, wordfreq)
getpairwithprobability(p_backward, wordfreq)

word_horizon = []

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
	p_forward_item = map(lambda t: (t[0], sum(map(lambda m:m[1], t[1].items()))), p_forward.items())
	p_backward_item = dict(map(lambda t: (t[0], sum(map(lambda m:m[1], t[1].items()))), p_backward.items()))
	print p_forward_item[:20]
	print p_backward_item.items()[:20]
	for word1, p in p_forward_item:
		p_total = 0
		if word1 in p_backward_item:
			p_total = p - p_backward_item[word1]
		print (word1, 1 if p_total>0 else -1)

