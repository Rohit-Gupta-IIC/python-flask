#http://localhost:5000/flask/
#output will be  404 eror
#http://localhost:5000/python/
#output will be  Hello Python
#http://localhost:5000/flask
#output will be Hello Flask


from flask import Flask
app = Flask(__name__)

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

if __name__ == '__main__':
   app.run()
