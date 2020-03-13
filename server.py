from flask import Flask, render_template, url_for
from form import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '906fbd7219bb638e86f156dc5eac6512'

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
	app.run(debug=True)