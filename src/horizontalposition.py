def appendhorizontalposition(sentence, result):
	"""
	position means [-1,1] continously.
	@sentence: 	[a,b,c]
	@result: 	{a:[p,times], ...}
	"""
	def addto(container, value, p):
		if value in container:
			container[value][0] += p
			container[value][1] += 1
		else:
			container[value] = [p, 1]

	length = len(sentence)
	if length == 0:
		return
	elif length == 1:
		addto(result, sentence[0], 0)
	else:
		step = 2.0 / (length - 1)
		init = -1.0
		for tmp in sentence:
			typeofobj = type(tmp)
			if typeofobj == 'str':
				addto(result, tmp, init)
				init += step
			elif typeofobj == 'list':
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


