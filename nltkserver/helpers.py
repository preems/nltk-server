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