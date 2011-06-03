from tools 	import *
from intimacy 	import *
from horizontal import *
from verticle 	import *

filenames = ['network.txt', 'novel1.txt', 'novel2.txt', 'novel3.txt', 'raw.txt','cnn.com-us.txt','telegraph.co.uk.txt']
#filenames = ['telegraph.co.uk.txt']

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


