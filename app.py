from flask import Flask, render_template
from data import Articles

app = Flask(__name__)

Articles = Articles()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/articles')
def posts():
    return render_template('articles.html', articles = Articles)

@app.route('/article/<string:id>/')
def post(id):
    return render_template('article.html', id=id)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return 'contact'

if __name__=='__main__':
    app.run(debug=True)
