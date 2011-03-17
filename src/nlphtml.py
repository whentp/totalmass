class htmlstep:
	def __init__(self):
		self.sentences = []

	def addsentence(self, wordlist):
		sb = []
		for x in wordlist:
			sb += ['<span class="word" style="padding-top:',x[1].__str__(),'px">',x[0],'</span>']
		res = ''.join(sb)
		self.sentences.append('<div class="sentence">'+res+'<div class="sentence_end"></div></div>' if len(res) > 0 else '')
	
	def out(self):
		return """<!DOCTYPE HTML>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title></title>
		<link rel="stylesheet" href="nlpstyle.css" />
	</head>
	<body>""" + ''.join(self.sentences) +"</body></html>"

