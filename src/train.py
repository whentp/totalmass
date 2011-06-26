from tools 	import *
from intimacy 	import *
from horizontal import *
from verticle 	import *

#filenames = ['telegraph.co.uk.txt']
filenames = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt','6.txt','7.txt']

filenames = [
		#'network.txt': 2,
		#'cnn.com-us.txt':4,
		#'telegraph.co.uk.txt':3,
		#'telegraph.co.uk.spaceseparated.txt':'4',
		'guardian.co.uk-china.txt',
		'guardian.co.uk-integrated.txt',
		'guardian.co.uk.txt',
		'xinhuanet.com-china.txt',
		#'spain.txt':3,'france.txt':1,
		'1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt', '7.txt',
		'fyp.txt',
		'fyp-cs.txt',
		#'novel1.txt',
		#'novel2.txt',
		#'novel3.txt',
		#'novel4.txt'
		]

#filenames = ['network.txt', 'novel1.txt', 'novel2.txt', 'novel3.txt', 'raw.txt','cnn.com-us.txt','telegraph.co.uk.txt']
filenames = ['network.txt', 'novel1.txt', 'novel2.txt', 'novel3.txt']#, 'raw.txt','cnn.com-us.txt','telegraph.co.uk.txt']

#Load files
rawtext = ' \n '.join(map(lambda x: loadrawtextfile('test_data/'+x), filenames))
sentencelist = getsentencelist(rawtext)

wordfreq = countwords(getwordlist(rawtext), 1)
writetofile('wordfreq.lib', repr(wordfreq))

wordintimacy = getintimacy(sentencelist, wordfreq)
writetofile('wordintimacy.lib', repr(wordintimacy))

result = {}
for tmp in sentencelist:
	appendhorizontalposition_norepeat(tmp, result)
wordhorizontal = gethorizontalposition(result)
writetofile('wordhorizontal.lib', repr(wordhorizontal))

wordverticle = getverticle(sentencelist, wordfreq)
writetofile('wordverticle.lib', repr(wordverticle))


