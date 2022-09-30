import flask

app = flask.Flask(__name__)
#app.config["DEBUG"] = True

@app.route('/')
@app.route("/home")
def home():
    return "<h1>Hello, it's me, Hello from the outside</h1><br> <h3>holllllllla </h3>"

@app.route('/user/<username>')
def show_user(username):
    return "<h1>UserName: "+ username+"</h1>"
    
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "<h1>post_id: "+str(post_id)+ "</h1>"

@app.route('/about')
def about():
    return "<h1>About Page</h1>"
    #return render_template('mess.html', mess="About Page")

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)