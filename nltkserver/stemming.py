from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
from flask import abort
from helpers import ret_success
from helpers import ret_failure
from helpers import parse_input

LancasterSt = LancasterStemmer()
PorterSt = PorterStemmer()

def stemmer(method,data):
	data = parse_input(data)
	if data == False:
		return ret_failure(703)
	else:
		res=[]
		if method == "lancaster":
			for word in data:
				try:
					res.append([word,LancasterSt.stem(word)])
				except:
					return ret_failure(702)
		elif method == "porter":
			for word in data:
				try:
					res.append([word,PorterSt.stem(word)])
				except:
					return ret_failure(702)
		else:
			abort(404)
		return ret_success(res)
