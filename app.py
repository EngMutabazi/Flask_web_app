from flask import Flask, render_template, url_for

app = Flask(__name__) # This is the name of the module

posts= [
    {
    'author': 'van rossum',
    'title': 'Python programming',
    'content': 'First content of the book!',
    'date_posted': 'April 20, 2022'
    },
    {
    'author': 'Bjarne Stroustrup',
    'title': 'c++ programming',
    'content': 'second content of the book!',
    'date_posted': 'May 28, 2022'
    },

    
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts= posts)

@app.route("/about")
def about():
    return render_template('about.html')

#set flask app run in debug mode
if __name__== '__main__':
    app.run(debug=True)