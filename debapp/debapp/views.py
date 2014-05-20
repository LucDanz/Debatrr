from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from debapp import app, db, lm, oid
from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN



@app.route('/login', methods = ['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        #validate
	#login_user(user)
	flash("Logged in successfully")
    return render_template('login.html', 
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])

@app.route('/dashboard')
@login_required
def dashboard():
	flash("this is the dashboard")
