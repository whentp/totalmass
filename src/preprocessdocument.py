"""
The above codes are for dealing with documents downloaded from http://www.gutenberg.org/catalog/
By whentp
"""
import re, sys

def process(filename):
	rawfile = open(filename, 'r')
	# remove the first 30 and last 360 lines, strip spaces, and keep CR and LF
	lines = map(lambda x1: '*** ***' if len(x1) == 0 else x1,
			map(lambda x: x.strip(),
				rawfile.readlines()[29:-360]))
	rawfile.close()
	rawtext = ' '.join(lines).lower()
	rawtext = rawtext.replace('mr.', 'mr')
	rawtext = rawtext.replace('mrs.', 'mrs')
	rawtext = rawtext.replace('--', ' -- ')
	rawtext = rawtext.replace('_', '')

	rawtext = rawtext.replace('*** ***', '\n')
	return rawtext
	

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage: preprosessdocument.py rawfile.txt"
	else:
		rawtext = process(sys.argv[1])
		if len(sys.argv) == 3:
			open(sys.argv[2],'w').write(rawtext)
		else:
			print rawtext
