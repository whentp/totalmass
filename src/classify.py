from tools 	import *
from intimacy 	import *
from horizontal import *
from verticle 	import *
from intimacy 	import *
from math 	import *

wordfreq = loadandeval('wordfreq.lib')
topwords = wordfreq.items()
topwords.sort(valuedesc)
topwords = dict(topwords[:int(len(topwords)/200)])

wordhorizontal = loadandeval('wordhorizontal.lib')

filenames = {
		'1.txt': 1,
		'2.txt': 1,
		'3.txt': 1,
		'4.txt': 1,
		'5.txt': 1,
		'6.txt': 1,
		'7.txt': 1,
		'network.txt': 2}

# read files
files = []
for filename, tag in filenames.items():
	raw = open('test_data/' + filename, 'r')
	txt = filter(lambda x: len(x) > 0,
			map(lambda x: x.strip(), 
				raw.read().replace('\r', '\n').split('\n\n\n')))
	for t in txt:
		files.append({
			'filename': filename,
			'tag': tag,
			'txt': t,
			'sentences': getsentencelist(t)})

print len(files)
ppppp()

colors = {'1': "'b'", '2': "'r'"}

for f in files:
	t =  filter(lambda x: x[0] in topwords, getverticle(f['sentences'], wordfreq).items())
	m_v = sum(map(lambda x: x[1], t)) / len(t)

	result = {}
	for tmp in f['sentences']:
		appendhorizontalposition(tmp, result)
	res = map(lambda x: abs(x[1] - wordhorizontal[x[0]]),
			filter(lambda x: x[0] in wordhorizontal, 
				gethorizontalposition(result).items()))
	m_h = sum(res) / len(res)

	t = getintimacy(f['sentences'], wordfreq).items()
	m_i = sum(map(lambda x: x[1], t)) / len(t)
	
	print m_h, ' ', m_v, ' ', m_i, ' ',  f['tag'], ';'
