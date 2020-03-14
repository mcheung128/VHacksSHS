from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from form import RegistrationForm, LoginForm
from datetime import datetime
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = '906fbd7219bb638e86f156dc5eac6512'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	posts = db.relationship('Drive', backref='driver', lazy=True)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Drive(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	time_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	time_driven = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	day_night = db.Column(db.String(10), nullable=False)
	weather = db.Column(db.String(60), unique=True, nullable=False)
	#DO NOT CHANGE 'user.id', to 'User.id'; this is ok, and necessary.
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


	def __repr__(self):
		return f"User('{self.time_posted}', '{self.time_driven}', '{self.weather}')"

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
	app.run(debug=True)