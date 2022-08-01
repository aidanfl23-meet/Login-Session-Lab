from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supers-secret-key'

@app.route('/', methods=['GET', 'POST'] ) # What methods are needed?
def home():
	if request.method == 'GET':
		return render_template('home.html')
	else:
		quote = request.form["quote"]
		name = request.form["name"]
		age = request.form["age"]
		login_session["quote"] = quote
		login_session["name"] = name
		login_session["age"] = age 		
		return redirect(url_for('display'))


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():
	return render_template('display.html' , logi = login_session) # What variables are needed?


@app.route('/thanks')
def thanks():
	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(port=8329, debug=True)