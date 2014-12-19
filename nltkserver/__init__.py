import nltk
import json
from helpers import ret_success
from helpers import ret_failure



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
	if data == None:
		return ret_failure(701)
	try:
		data = json.loads(data)
	except:
		return ret_failure(703)
	try:
		res = nltk.pos_tag(data)
		return ret_success(res)
	except:
		return ret_failure(702)