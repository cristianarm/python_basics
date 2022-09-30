from flask import Flask, render_template  

app = Flask(__name__)
#app.config["DEBUG"] = True

@app.route("/")
@app.route("/home")
def home():
    return render_template('mess.html', mess="Hello, it's me, Hello from the outside, Its raining ")

@app.route("/site")
def site():
    return "<h1>Welcome to ...... site</h1>"
    #return render_template('mess.html', mess="Welcome to ...... site")

@app.route("/about")
def about():
    #return "<h1>About Page</h1>"
    return render_template('mess.html', mess="About Page")

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)