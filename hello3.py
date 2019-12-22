from flask import Flask
from flask import render_template_string
app=Flask(__name__)
@app.route("/")
def hello_world():
	html="""
	<html>
	<h1>Hello World</h1>
	<ul>
	{% for a in authors%}
	<li>{{a}}</li>
	{%endfor%}
	</ul>
	</html>
	"""
	authors=["Harry","Sharon","Alexa"]
	rhtml=render_template_string(html,authors=authors)
	return rhtml