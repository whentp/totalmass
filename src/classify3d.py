from tools 	import *
from intimacy 	import *
from horizontal import *
from verticle 	import *
from intimacy 	import *
from math 	import *

wordfreq = loadandeval('wordfreq.lib')
topwords = wordfreq.items()
topwords.sort(valuedesc)
#topwords = dict(topwords[:int(len(topwords)/30)])
#topwords = dict(gettopitems(topwords, 0.999999))

# use all.
topwords = dict(topwords)

#printpairs(topwords)
#quit()

wordhorizontal = loadandeval('wordhorizontal.lib')

filenames = {
		#'network.txt': 2,
		#'cnn.com-us.txt':4,
		#'telegraph.co.uk.txt':3,
		#'telegraph.co.uk.spaceseparated.txt':'4',
		'guardian.co.uk-china.txt':2,
		#'guardian.co.uk-integrated.txt':5,
		'xinhuanet.com-china.txt':2,
		'spain.txt':3,'france.txt':1,
		'1.txt': 1, '2.txt': 1, '3.txt': 1, '4.txt': 1, '5.txt': 1, '6.txt': 1, '7.txt': 1,
		'fyp.txt': 3,
		'fyp-cs.txt': 3,
		'novel1.txt': 5,
		'novel5.txt': 5,
		'novel4.txt': 5,
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
			if t < 2:
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
	
	# divideby 
	# This feature is adopted.
	m_v = sum(map(lambda x: x[1], t)) / divideby(len(t))

	# horizontal position is useless.
	result = {}
	for tmp in f['sentences']:
		appendhorizontalposition(tmp, result)
	res = map(lambda x: abs(x[1] - wordhorizontal[x[0]]),
			filter(lambda x: x[0] in wordhorizontal, 
				gethorizontalposition(result).items()))
	m_h = sum(res) / divideby(len(res))

	# This feature is adopted.
	t = getintimacy(f['sentences'], wordfreq).items()
	m_i = sum(map(lambda x: abs(x[1]), t)) / divideby(len(t))
	
	#print m_v, ' ', m_i, ' ',  f['tag'], ';'
	print m_v, ' ', m_h, ' ', m_i, ' ',  f['tag'], ';'


# Just for matlab

print "];"
print """
plot3(a(find(a(:,4)==1),1),a(find(a(:,4)==1),2),a(find(a(:,4)==1),3),'ro','MarkerSize',2);
hold on;
plot3(a(find(a(:,4)==2),1),a(find(a(:,4)==2),2),a(find(a(:,4)==2),3),'go','MarkerSize',2);
hold on;
plot3(a(find(a(:,4)==3),1),a(find(a(:,4)==3),2),a(find(a(:,4)==3),3),'bo','MarkerSize',2);
hold on; 
plot3(a(find(a(:,4)==4),1),a(find(a(:,4)==4),2),a(find(a(:,4)==4),3),'yo','MarkerSize',2);
hold on;
plot3(a(find(a(:,4)==5),1),a(find(a(:,4)==5),2),a(find(a(:,4)==5),3),'ko','MarkerSize',2);
hold on;
plot3(a(find(a(:,4)==6),1),a(find(a(:,4)==6),2),a(find(a(:,4)==6),3),'mo','MarkerSize',2);
"""
