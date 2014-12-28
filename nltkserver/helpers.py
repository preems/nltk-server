import json
from flask import jsonify
from errorcodes import error_code

def ret_success(result):
	res={}
	res["status"]="success"
	res["result"]=result
	return jsonify(res)

def ret_failure(code):
	res={}
	res["status"]="error"
	res["error_code"]=code
	res["error_message"]=error_code[code]
	return jsonify(res)

def parse_input(data):
	try:
		data = json.loads(data)
		return data
	except:
		return False

def penn_to_wn(tag):
	if tag in ['n','v','r','a']:
		return tag
	elif tag in ['NN', 'NNS', 'NNP', 'NNPS']:
		return 'n'
	elif tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
		return 'v'
	elif tag in ['RB', 'RBR', 'RBS']:
		return 'r'
	elif tag in ['JJ', 'JJR', 'JJS']:
		return 'a'
	else:
		return 'n'