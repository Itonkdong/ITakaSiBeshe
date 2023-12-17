from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def getIndex():
    return "Hello World!"



@app.route('/login')
def fuck():
    return "Login"



if __name__ == '__main__':
    app.run(debug=True)