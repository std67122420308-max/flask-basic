from flask import Flask
import uuid

app = Flask(__name__)

@app.route('/')
def index():
  return f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FLASK BASIS</title>
</head>
<body>
  <h1>HOME Page</h1>
  <hr>
</body>
</html>"""

@app.route('/name')
def name():
  return f'<h1>nontagorn</h1>'


@app.route('/User/<username>')
def user(username):
  return f'<h1>My name is: {username}</h1>'

@app.route('/calculater/addition/<int:a>/<int:b>')
def addition(a, b):
  result = a + b
  return f'<h1>{a} + {b} = {a+b}</h1>'


@app.route('/calculatee/subtraction/<int:a>/<int:b>')
def subtraction(a, b):
  result = a - b
  return f'<h1>{a} - {b} = {a-b}</h1>'

@app.route('/calculatee/multiplication/<int:a>/<int:b>')
def multiplication(a, b):
  result = a * b
  return f'<h1>{a} * {b} = {result}</h1>'

@app.route('/calculatee/division/<int:a>/<int:b>')
def division(a, b):
  result = a / b
  return f'<h1>{a} / {b} = {result}</h1>'


@app.route('/secretkey/<uuid:sk>')
def my_secretkey(sk):
  return f'<h1>My secret key is: {sk}</h1>'


  # if  __name__=='__main__':
  # app.run(debug=True)