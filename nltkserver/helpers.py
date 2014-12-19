import json
from errorcodes import error_code

def ret_success(result):
	res={}
	res["status"]="success"
	res["result"]=result
	return json.dumps(res)

def ret_failure(code):
	res={}
	res["error_code"]=code
	res["error_message"]=error_code[code]
	return json.dumps(res)