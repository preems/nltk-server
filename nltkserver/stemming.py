import nltk
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import EnglishStemmer
from nltk.stem import WordNetLemmatizer
from flask import abort
from helpers import ret_success
from helpers import ret_failure
from helpers import parse_input
from helpers import penn_to_wn



LancasterSt = LancasterStemmer()
PorterSt = PorterStemmer()
SnowballSt = EnglishStemmer()
WordnetLm = WordNetLemmatizer()

def stemmer(method,data):
	"""
	Takes an array of words in JSON format.
	"""
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
		elif method == 'snowball':
			for word in data:
				try:
					res.append([word,SnowballSt.stem(word)])
				except:
					return ret_failure(702)
		else:
			abort(404)
		return ret_success(res)

def lemmatize(method,data):
	"""
	Takes an array of words or array of tupples containing words and pos tags.
	Both Penn and Wordnet tags are supported
	"""
	data = parse_input(data)
	if data == False:
		return ret_failure(703)
	else:
		res=[]
		if method == "wordnet":
			for word in data:
				try:
					if type(word) is list:
						res.append([word[0],WordnetLm.lemmatize(word[0],penn_to_wn(word[1]))])
					else:	
						res.append([word,WordnetLm.lemmatize(word)])
				except LookupError: 
					return ret_failure(704)
				except:
					return ret_failure(702)
		else:
			abort(404)
		return ret_success(res)
