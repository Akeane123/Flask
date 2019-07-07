from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Andrew Keane',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date': 'July 06, 2019'
    },
    {
        'author': 'Jane Keane',
        'title': 'Blog Post 2',
        'content': 'first post content',
        'date': 'July 21, 2019'
    }
]

# We need to add the path of the app to our environment variable, using the following: set FLASK_APP=flask_test.py. See instructions in README file for setting this up. 


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts, ) # Note that we can pass arguments into our template

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)