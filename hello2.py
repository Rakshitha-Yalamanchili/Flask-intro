from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello_world():
	html="""
	<html>
	<h1>Hello World</h1>
	{l}
	</html>
	"""
	authors=["Harry","Sharon"]
	l="<ul>"
	l+="\n".join(["<li>{a}</li>".format(a=author) for author in authors])
	l+="</ul>"
	return html.format(l=l)