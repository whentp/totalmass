from tools 	import *
from intimacy 	import *
from horizontal import *
from verticle 	import *
from intimacy 	import *
from math 	import *

filenames = {
		'network.txt': 2,
		'cnn.com-us.txt':2,
		'telegraph.co.uk.txt':2,
		'telegraph.co.uk.spaceseparated.txt':2,
		'guardian.co.uk-china.txt':2,
		'guardian.co.uk-integrated.txt':2,
		'xinhuanet.com-china.txt':3,
		#'spain.txt':3,'france.txt':2,
		'1.txt': 1, '2.txt': 1, '3.txt': 1, '4.txt': 1, '5.txt': 1, '6.txt': 1, '7.txt': 1,
		'fyp.txt': 5,
		'fyp-cs.txt': 5,
		'novel1.txt': 6,
		'novel5.txt': 6,
		'novel4.txt': 6,
		}

filenames = {
		#'network.txt': 2,
		'cnn.com-us.txt':4,
		'telegraph.co.uk.txt':3,
		#'telegraph.co.uk.spaceseparated.txt':3,
		'guardian.co.uk-china.txt':2,
		'guardian.co.uk-integrated.txt':2,
		'xinhuanet.com-china.txt':1,
		#'spain.txt':3,'france.txt':2,
		#'1.txt': 1, '2.txt': 1, '3.txt': 1, '4.txt': 1, '5.txt': 1, '6.txt': 1, '7.txt': 1,
		#'fyp.txt': 5,'fyp-cs.txt': 5,
		'novel1.txt': 6,'novel5.txt': 6,'novel4.txt': 6,
		}

rawtext = ' \n '.join(map(lambda x: loadrawtextfile('test_data/'+x), filenames.keys()))
sentencelist = getsentencelist(rawtext)

wordfreq = countwords(getwordlist(rawtext), 1)
#writetofile('wordfreq.lib', repr(wordfreq))

wordintimacy = getintimacy(sentencelist, wordfreq)
#writetofile('wordintimacy.lib', repr(wordintimacy))

result = {}
for tmp in sentencelist:
	appendhorizontalposition_norepeat(tmp, result)
wordhorizontal = gethorizontalposition(result)
#writetofile('wordhorizontal.lib', repr(wordhorizontal))

wordverticle = getverticle(sentencelist, wordfreq)
#writetofile('wordverticle.lib', repr(wordverticle))

#wordfreq = loadandeval('wordfreq.lib')
topwords = wordfreq.items()
topwords.sort(valuedesc)
#topwords = dict(topwords[:int(len(topwords)/30)])

#topwords = dict(gettopitems(topwords, 0.50))

# use all.
topwords = dict(topwords)

#gettopitems(topwords, 0.50)
#printpairs(topwords)
#quit()

#wordhorizontal = loadandeval('wordhorizontal.lib')

# read files
files = []
for filename, tag in filenames.items():
	raw = open('test_data/' + filename, 'r')
	txt = filter(lambda x: len(x) > 0,
			map(lambda x: x.strip(), 
				raw.read().replace('\r', '\n').split('\n\n\n\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')))
	for t in txt:

		tmpsentencelist = getsentencelist(t);
		while(1):
			t = len(tmpsentencelist)
			if t > 20:
				t = 20
			if t < 20:
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
