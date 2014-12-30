from nltk.tag.stanford import NERTagger
from helpers import ret_success
from helpers import ret_failure

def tagger(data):
	try:
		st=NERTagger('./nltk-data/StanfordNER/english.all.3class.distsim.crf.ser.gz','./nltk-data/StanfordNER/stanford-ner.jar')
	except:
		return ret_failure(705)
	#try:
	tag = st.tag(data.split())
	#except:
	#	return ret_failure(702)
	return ret_success(tag)