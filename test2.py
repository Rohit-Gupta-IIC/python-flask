#http://localhost:5000/blog/11
#output will be Blog number 11
#http://localhost:5000/rev/11.1
#output will be Revision Number 11.1


from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

if __name__ == '__main__':
   app.run()
