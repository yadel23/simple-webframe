from flask import Flask, render_template, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import secrets
from forms import RegistrationForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '6899aed57fc9a147782e72f9bde1ed9a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)

def __repr__(self):
  return f"User('{self.username}', '{self.email}')"

@app.route("/")
def hello_world():
    return '<p> Hello World!!! </p>'
 

@app.route('/home')
def home():
  return render_template('home.html', subtitle = 'Home Page subtitle')
    
 
@app.route('/layout')
def layout():
  return render_template('layout.html', text = 'for the layout page testing txt')
 
@app.route('/second_page')
def second_page():
  return render_template('second_page.html', subtitle = 'Second Page subtitle')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # if so - send to home page
    return render_template('register.html', title='Register', form=form) 
    
    
if __name__ == '__main__':
  app.run(debug = True, host = '0.0.0.0')