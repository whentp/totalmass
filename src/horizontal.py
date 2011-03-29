from types import *

def addto(container, value, p):
	if value in container:
		container[value][0] += p
		container[value][1] += 1
	else:
		container[value] = [p, 1]

def appendhorizontalposition(sentence, result):
	"""
	position means [-1,1] continously.
	@sentence: 	[a,b,c]
	@result: 	{a:[p,times], ...}
	"""
	length = len(sentence)
	if length == 0:
		return
	elif length == 1:
		addto(result, sentence[0], 0.0)
	else:
		step = 2.0 / (length - 1)
		init = -1.0
		for tmp in sentence:
			typeofobj = type(tmp)
			if typeofobj is StringType:
				addto(result, tmp, init)
				init += step
			elif (typeofobj is TupleType) or (typeofobj is TupleType):
				gethorizontalposition(tmp, result)

def appendhorizontalposition_norepeat(sentence, result):
	"""
	position means [-1,1] continously. But this function will ignore words which appeared in the same sentence twice or more.
	@sentence: 	[a,b,c]
	@result: 	{a:[p,times], ...}
	"""
	length = len(sentence)
	if length == 0:
		return
	elif length == 1:
		addto(result, sentence[0], 0.0)
	else:
		checkrepeated = {}
		for tmp in sentence:
			if tmp in checkrepeated:
				checkrepeated[tmp] = 1
			else:
				checkrepeated[tmp] = 0
		step = 2.0 / (length - 1)
		init = -1.0
		for tmp in sentence:
			if checkrepeated[tmp]:
				continue
			typeofobj = type(tmp)
			if typeofobj is StringType:
				addto(result, tmp, init)
				init += step
			elif (typeofobj is TupleType) or (typeofobj is TupleType):
				gethorizontalposition(tmp, result)

def gethorizontalposition(tmp_result):
	"""
	@tmp_result: 	{a:[p, times], ...}
	return value: 	{a: \bar(p), ...}
	"""
	result = {}
	for k, v in tmp_result.items():
		result[k] = v[0] / v[1]
	return result

