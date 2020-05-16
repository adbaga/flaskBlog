from flask import render_template, url_for, flash, redirect
from FlaskBlog.models import User, Post
from FlaskBlog import app
from FlaskBlog.forms import RegistrationForm, LoginForm,QuestionForm




posts = [

{
	'author': 'Benny Hellyo',
	'title': 'Gardening in Tight Spaces',
	'content': 'Green Life in A Big City',
	'date_posted': 'May 4, 2020'
},


{
	'author': 'Big Op',
	'title': 'Life of Ants',
	'content': 'Second book about ant colonies',
	'date_posted': 'May 6, 2020'
}

]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)\



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



@app.route("/question", methods=['GET', 'POST'])
def question():
    form = QuestionForm()
    if form.validate_on_submit():
        flash(f'Question is submitted and we will the answer to {form.email.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('question.html', title='Register', form=form)
