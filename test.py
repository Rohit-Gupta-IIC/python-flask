#http://localhost:8080/
#debugging is set to true
#port is changed from 5000 to 8080

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"

if __name__ == '__main__':
   app.run(port=8080,debug=True)
