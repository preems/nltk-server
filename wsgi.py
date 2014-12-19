from flask import Flask, request, Response
import nltkserver
application = app = Flask(__name__)

@app.route('/word_tokenize',methods=['POST'])
def word_tokenize():
    return nltkserver.word_tokenize(request.data)

@app.route('/sent_tokenize',methods=['POST'])
def sent_tokenize():
    return nltkserver.sent_tokenize(request.data)

@app.route('/pos_tag',methods=['POST'])
def pos_tag():
    return nltkserver.pos_tag(request.data)

if __name__ == '__main__':
    app.run()