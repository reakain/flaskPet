from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True
comments = []
@app.route('/', methods=["GET","LOGIN"])
def index():
	if request.method == "LOGIN":
		return render_template("main_page.html", comments=comments)
		
	comments.append(request.form["uname"])
	return redirect(url_for('index'))

@app.route('/wibble')
def wibble():
	return 'wibblyyyyy!'