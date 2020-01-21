from flask import Flask
from flask import render_template
app=Flask(__name__)

A={'Poe':'LAST_NAME:POE','Joe':'LAST_NAME:JOE'}

@app.route('/')
def auth():
	return render_template('routing1.html')

@app.route('/authors/<last_name>')
def author(last_name):
	return render_template('routing2.html',author=A[last_name])