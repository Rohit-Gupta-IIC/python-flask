#http://localhost:5000/hello/60
#output will be your result is pass
#http://localhost:5000/hello/30
#output will be you result is fail

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<int:score>')
def hello_name(score):
   return render_template('hello.html', marks = score)

if __name__ == '__main__':
   app.run(debug = True)
