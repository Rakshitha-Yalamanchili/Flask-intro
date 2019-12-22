from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello_world():
	html="""
	<html>
	<h1>Hello World</h1>
	</html>
	"""
	return html