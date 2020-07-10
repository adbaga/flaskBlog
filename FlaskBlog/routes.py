from flask import render_template, url_for, flash, redirect, request
from FlaskBlog.models import User, Post
from FlaskBlog import app, db, bcrypt
from FlaskBlog.forms import RegistrationForm, LoginForm,QuestionForm, UpdateAccountForm
import datetime
from flask_login import login_user, current_user, logout_user, login_required
#from info import DateTime


now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")


#from FlaskBlog.info import DateTime

infoSidebar = {
    'time': now,
    'latest': "YA YA"
}



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


#time = DateTime.current_time()


@app.route("/")
#def layout():
    #info = time()
    #return render_template('layout.html', infoSidebar=info)

@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')




@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
        #flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

# @app.route("/login", methods=['GET', 'POST'])
# def login():

#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and bcrypt.check_password_hash(user.password, form.password.data):
#             login_user(user, remember=form.remember.data)
#             next_page = request.args.get('next')
#             return redirect(next_page) if next_page else (url_for('home')) #if account exist, redirect to account page
    #     else:
    #         flash('Login Unsuccessful. Please check email and password', 'danger')
        
    # return render_template('login.html', title='Login', form=form)



@app.route("/question", methods=['GET', 'POST'])
@login_required
def question():
    form = QuestionForm()
    if form.validate_on_submit():
        flash(f'Question is submitted and we will the answer to {form.email.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('question.html', title='Register', form=form)



@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    form = UpdateAccountForm()
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',image_file=image_file, form=form)

# @app.route("/account")
# @login_required
# def account():
#     image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
#     return render_template('account.html', title='Profile', image_file=image_file)
    # return redirect(url_for('/home'))