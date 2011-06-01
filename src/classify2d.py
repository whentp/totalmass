from tools 	import *
from intimacy 	import *
from horizontal import *
from verticle 	import *
from intimacy 	import *
from math 	import *

wordfreq = loadandeval('wordfreq.lib')
topwords = wordfreq.items()
topwords.sort(valuedesc)
topwords = dict(topwords[:int(len(topwords)/300)])

wordhorizontal = loadandeval('wordhorizontal.lib')

filenames = {
		#'1.txt': 1,
		#'2.txt': 1,
		#'3.txt': 1,
		#'4.txt': 1,
		#'5.txt': 1,
		#'6.txt': 1,
		#'7.txt': 1,
		#'network.txt': 2,
		#'cnn.com-us.txt':1,
		'telegraph.co.uk.txt':2,
		#'telegraph.co.uk.spaceseparated.txt':'1',
		'xinhuanet.com-china.txt':3,
		#'fyp.txt': 3
		}

# read files
files = []
for filename, tag in filenames.items():
	raw = open('test_data/' + filename, 'r')
	txt = filter(lambda x: len(x) > 0,
			map(lambda x: x.strip(), 
				raw.read().replace('\r', '\n').split('\n\n\n\n')))
	for t in txt:

		tmpsentencelist = getsentencelist(t);
		while(1):
			t = len(tmpsentencelist)
			if t > 10:
				t = 10
			if t == 0:
				break
			head, tails = tmpsentencelist[:t-1], tmpsentencelist[t:]
			files.append({
				'filename': filename,
				'tag': tag,
				'txt': t,
				'sentences': head})
			tmpsentencelist = tails

#print len(files)
#ppppp()

print "a=["

for f in files:
	t =  filter(lambda x: x[0] in topwords, getverticle(f['sentences'], wordfreq).items())
	m_v = sum(map(lambda x: x[1], t)) / (len(t) if len(t)!=0 else 1)

	result = {}
	for tmp in f['sentences']:
		appendhorizontalposition(tmp, result)
	res = map(lambda x: abs(x[1] - wordhorizontal[x[0]]),
			filter(lambda x: x[0] in wordhorizontal, 
				gethorizontalposition(result).items()))
	m_h = sum(res) / (len(res) if len(res)!=0 else 1)

	t = getintimacy(f['sentences'], wordfreq).items()
	#m_i = sum(map(lambda x: abs(x[1]), t)) / (len(t) if len(t)!=0 else 1)
	
	print m_h, ' ', m_v, ' ',  f['tag'], ';'


# Just for matlab

print "];"
print """
scatter(a(find(a(:,4)==1),1),a(find(a(:,4)==1),2),'r','.'); 
hold on; 
scatter(a(find(a(:,4)==2),1),a(find(a(:,4)==2),2),'b','.'); 
hold on; 
scatter(a(find(a(:,4)==3),1),a(find(a(:,4)==3),2),'g','.');
hold on; 
scatter(a(find(a(:,4)==4),1),a(find(a(:,4)==4),2),'y','.');
"""
