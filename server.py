from flask import Flask, render_template,request, redirect,session
app = Flask(__name__)
app.secret_key = "secreto"


@app.route('/')
def index():
    if not 'count' in session:
        session['count'] = 0
        session['count'] += 1
    return render_template("index.html", count = session['count'])


@app.route('/submit', methods=['POST'])
def submit():
    if request.form['action'] == 'increment':
        session['count'] += 1
    elif request.form['action'] == 'reset':
        session['count'] = 0
    return redirect('/')


app.run(debug=True)

