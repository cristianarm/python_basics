import flask

app = flask.Flask(__name__)

#@app.route('/', methods=['GET'])
@app.route('/')
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)