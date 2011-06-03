import sys

filename = sys.argv[1]
raw = '\n'.join((map(lambda x: x.strip(), open(filename, 'r').readlines())))
cutter = map(lambda x: x.strip(), raw.split("\n\n\n\n\n"))
cutter = filter(lambda x: len(x)>0, cutter)
print len(cutter)

