from flask import Flask, render_template  
from flask import jsonify

app = Flask(__name__)

@app.route('/')
@app.route("/home")
def home():
    return render_template('hello.html')
    
@app.route('/mathapi/',defaults={'x': 1,'y':1})
@app.route('/mathapi/<int:x>/<int:y>/',  methods = ['GET'])
def math(x, y):
    result = x + y # Sum x,t -> result
    response = '%d + %d = %d' %(x, y, result) #Buld response
    #return response #Return response
    return render_template('mess.html',mess= response)

@app.route('/mathapijson/',defaults={'x': 1,'y':1})
@app.route('/mathapijson/<int:x>/<int:y>/', methods = ['GET'])
def mathjs(x, y):
    result = x + y #Sum x,t -> result
    data = {'x'  : x, 'y' : y, 'result' : result} #Buld arrary
    response = jsonify(data) #Convert to json
    response.status_code = 200 #Set status code to 200=ok
    response.headers['Link'] = 'http://localhost'
    return response #return json response

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)