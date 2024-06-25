from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')
@app.route('/experience')
def exp():
    return "Experiences"
@app.route('/project')
def pro():
    return "My Projects"

if __name__ == '__main__':
    app.run(debug = True)