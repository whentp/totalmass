filenames = {
		'1.txt', 1,
		'2.txt', 2,
		'3.txt', 3,
		'4.txt', 4,
		'5.txt', 5,
		'6.txt', 6,
		'7.txt',7}

# read files
files = []
for filename, tag in filenames.items():
	raw = open('text_data/' + filename, 'r')
	txt = filter(lambda x: len(x) > 0,
			map(lambda x: x.strip(), 
				raw.read().replace('\r', '\n').split('\n\n\n')))
	files.append({
		'filename': filename,
		'tag': tag,
		'txt': txt})


