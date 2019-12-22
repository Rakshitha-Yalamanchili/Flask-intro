from flask import Flask
from flask import render_template
app=Flask(__name__)
@app.route("/")
def hello_world():
	authors=["Ajay","Rohith"]
	return render_template("index.html",authors=authors)