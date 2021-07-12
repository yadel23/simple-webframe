from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__ == '__main__':
  app.run(debug = True, host = '0.0.0.0')