#!/usr/bin/python
from tools import *
import math

intimacy_steps = (30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

def getpairwithprobability(result, wordfreq):
	for k, tmp in result.items():
		factor = 1.0 / getwordfreq(wordfreq, k)
		for kk, vv in tmp.items():
			result[k][kk] = vv * factor

def getpairwithprobability_test(result, wordfreq):
	for k, tmp in result.items():
		for kk, vv in tmp.items():
			factor = 1.0 / getwordfreq(wordfreq, kk)
			result[k][kk] = vv * factor

def getpairprobability(sentencelist, wordfreq, p_forward, p_backward):
	for x in sentencelist:
		for cc in intimacy_steps:
			addpairwithvalue(x, cc, math.exp(- ((cc - 0)**2) / 2), p_forward)
			addreversedpairwithvalue(x, cc, math.exp(- ((cc - 0)**2) / 2), p_backward)

	getpairwithprobability(p_forward, wordfreq)
	getpairwithprobability(p_backward, wordfreq)


def getintimacy(sentencelist, wordfreq):
	p_forward = {}
	p_backward = {}
	getpairprobability(sentencelist, wordfreq, p_forward, p_backward)
	word_horizon = {}
	for word1, tmp in p_forward.items():
		p_total = 0.0
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
