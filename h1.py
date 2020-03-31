from flask import Flask
from flask import render_template
app=Flask(__name__)
@app.route("/")
def hello_world():
	l=['yjg','yj','gt','ef','d']
	return render_template("h1.html",l=l)