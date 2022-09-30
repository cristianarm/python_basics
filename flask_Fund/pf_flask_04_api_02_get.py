import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'},
    {'id': 3,
     'title': 'The lord of the ring',
     'author': 'J. R. R. Tolkien',
     'first_sentence': 'tThe Lord of the Rings is an epic high-fantasy novel by.',
     'published': '1954'},
    {'id': 4,
     'title': 'EL hombre en busca de sentido',
     'author': 'Victor Frankl',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1945'},
     {'id': 5,
    'title': 'Rueda del Tiempo',
    'author': 'Brandon Sanderson',
    'first_sentence': 'who knows',
    'published': '2019'},
    {'id': 6,
     'title': 'Cuando',
     'author': 'Daniel H. Pink',
     'first_sentence': '¡Cuánto hacen los hombres diariamente,sin saber lo que hacen!',
     'published': '2018'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/<int:id_book>', methods=['GET'])
def api_book(id_book):
    return jsonify(books[id_book])
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)