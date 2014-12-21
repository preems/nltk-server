import nltk
import json
from helpers import ret_success
from helpers import ret_failure
from helpers import parse_input

nltk.data.path.append('./nltk-data')

def word_tokenize(data):
	if data == None:
		return ret_failure(701)
	try:
		res = nltk.word_tokenize(data)
		return ret_success(res)
	except:
		return ret_failure(701)


def sent_tokenize(data):
	if data == None:
		return ret_failure(701)
	try:
		res = nltk.sent_tokenize(data)
		return ret_success(res)
	except:
		return ret_failure(702)

def pos_tag(data):
	data = parse_input(data)
	if data == False:
		return ret_failure(703)
	else:
		try:
			res = nltk.pos_tag(data)
			return ret_success(res)
		except LookupError: 
			return ret_failure(704)
		except:
			return ret_failure(702)