from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm, LoginForm
app = Flask(__name__) # This is the name of the module
app.config['SECRET_KEY']= '6150293ab0b283698350acd7307257a2'
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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        flash (f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', 
                           title= 'register', form=form)

@app.route("/login")
def login():
    form= LoginForm()
    return render_template('login.html', 
                           title= 'login', form=form)

#set flask app run in debug mode
if __name__== '__main__':
    app.run(debug=True)