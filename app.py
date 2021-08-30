from flask import Flask , render_template
from data import Articles

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/articles',methods=['GET','POST'])
def articles():
    list_data = Articles()
    return render_template('articles.html',data = list_data)

if __name__ == '__main__':
    app.run( debug=True)