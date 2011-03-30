#!/usr/bin/python
from tools import *
import math

def getintimacy(sentencelist, wordfreq):
	p_forward = {}
	p_backward = {}

	steps = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
	for x in sentencelist:
		for cc in steps:
			addpairwithvalue(x, cc, math.exp(- ((cc)**2) / 2), p_forward)
			addreversedpairwithvalue(x, cc, math.exp(- ((cc)**2) / 2), p_backward)

	getpairwithprobability(p_forward, wordfreq)
	getpairwithprobability(p_backward, wordfreq)

	word_horizon = {}

	for word1, tmp in p_forward.items():
		p_total = 0
		for word2, p in tmp.items():
			if (word2 in p_backward) and (word1 in p_backward[word2]):
				p_total += p - p_backward[word2][word1]
		word_horizon[word1] = p_total
	return word_horizon

# for test only
if __name__ == '__main__':
	rawtext=loadrawtextfile('test_data/novel1.txt')
	wordlist = getwordlist(rawtext)
	### wordfreq is the count of each word ###
	wordfreq = countwords(wordlist,1);
	sentencelist = getsentencelist(rawtext)
	print getintimacy(sentencelist, wordfreq)
