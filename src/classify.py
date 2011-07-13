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
topwords = dict(gettopitems(topwords, 0.8))

# use all.
#opwords = dict(topwords)

#printpairs(topwords)
#quit()

wordhorizontal = loadandeval('wordhorizontal.lib')
wordintimacy = loadandeval('wordintimacy.lib')
filenames = {
		'network.txt': 2,
		'cnn.com-us.txt':2,
		'telegraph.co.uk.txt':2,
		'guardian.co.uk-china.txt':2, 'guardian.co.uk-integrated.txt':2,
		'xinhuanet.com-china.txt':3,
		#'spain.txt':4,'france.txt':4,
		'1.txt': 1, '2.txt': 1, '3.txt': 1, '4.txt': 1, '5.txt': 1, '6.txt': 1, '7.txt': 1,
		'fyp.txt': 6,
		'fyp-cs.txt': 6,
		#'xulu.txt': 5
		'novel1.txt': 5,'novel2.txt': 5,
		#'andersen-s-fairy-tales.txt': 6
		}

# read files


sentencecount = 20

files = []
for filename, tag in filenames.items():
	raw = open('test_data/' + filename, 'r')
	txt = filter(lambda x: len(x) > 0,
			map(lambda x: x.strip(), 
				raw.read().replace('\r', '\n').replace('\n', ' ').split('\n\n\n\naaaaaaaaaaaaaaaaaaaaaaaaaaa')))
	for t in txt:
		tmpsentencelist = getsentencelist(t);
		while(1):
			t = len(tmpsentencelist)
			if t > sentencecount:
				t = sentencecount
			if t < sentencecount:
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
	#t =  getverticle(f['sentences'], wordfreq).items()
	
	# divideby 
	# This feature is adopted.
	m_v = sum(map(lambda x: x[1], t)) / divideby(len(t))

	# horizontal position is useless.
	#result = {}
	#for tmp in f['sentences']:
	#	appendhorizontalposition(tmp, result)
	#res = map(lambda x: abs(x[1] - wordhorizontal[x[0]]),
	#		filter(lambda x: x[0] in wordhorizontal, 
	#			gethorizontalposition(result).items()))
	#m_h = sum(res) / divideby(len(res))

	# This feature is adopted.
	t = getintimacy(f['sentences'], wordfreq).items()
	m_i = sum(map(lambda x: x[1], t)) / divideby(len(t))
	
	#t = filter(lambda x: x[0] in wordintimacy, t)
	#printpairs(map(lambda x: [x[0], x[1] - wordintimacy[x[0]]], t))

	#m_i = sum(map(lambda x: x[1] - wordintimacy[x[0]], t)) / divideby(len(t))
	
	#print m_v, ' ', m_i, ' ',  f['tag'], ';'
	print m_v, ' ', ' ', m_i, ' ',  f['tag'], ';'


# Just for matlab

print "];"

# For 3d
endmatlab3d = """
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
# For 2d
endmatlab2d = """
plot(a(find(a(:,3)==1),1),a(find(a(:,3)==1),2),'ro','MarkerSize',2);
hold on;
plot(a(find(a(:,3)==2),1),a(find(a(:,3)==2),2),'go','MarkerSize',2);
hold on;
plot(a(find(a(:,3)==3),1),a(find(a(:,3)==3),2),'bo','MarkerSize',2);
hold on; 
plot(a(find(a(:,3)==4),1),a(find(a(:,3)==4),2),'yo','MarkerSize',2);
hold on;
plot(a(find(a(:,3)==5),1),a(find(a(:,3)==5),2),'ko','MarkerSize',2);
hold on;
plot(a(find(a(:,3)==6),1),a(find(a(:,3)==6),2),'mo','MarkerSize',2);
"""

print endmatlab2d
