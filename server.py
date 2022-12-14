from flask import Flask, render_template, url_for, request, redirect, session, flash
from datetime import timedelta
import basic_functions
import data_base_functions

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(minutes=5)
# app.secret_key = "b/\n\xefp\xc6z\xaaj\xbd\x1fR=\x17.f%\xbf\xe7I\xd3"
app.secret_key = "11"

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        if len(session) == 0:
            username = 'Guest'
        else:
            username = session['user']
        return render_template('index.html', username=username)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if len(session) == 1:
        return redirect("/")
    if request.method == "GET":
        return render_template('login.html')
    if request.method == "GET" and "user" in session:
        return redirect('/')
    username = request.form['username']
    password = request.form['password']

    if data_base_functions.username_check(username):
        # hashed_password = data_base_functions.get_user_password(username)
        if data_base_functions.get_user_password(username) == password:
            session['user'] = username
            return redirect('/')
        else:
            error = "Incorrect username or password"
            return render_template('login.html', error=error)
    else:
        error = "Incorrect username or password"
        return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if len(session) == 1:
        return redirect("/")
    if request.method == 'GET':
        return render_template('register.html')
    user_name = request.form['username']
    user_password = request.form['password']
    if not data_base_functions.username_check(user_name):
        # user_password = basic_functions.get_hashed_password(user_password)
        data_base_functions.registration_to_db(user_name, user_password)
    else:
        error = "User name already in use. Try again."
        return render_template('register.html', error=error)
    return redirect(url_for('main'))


@app.route('/logout')
def logout():
    if len(session) == 0:
        return redirect("/")
    if "user" in session:
        session.pop("user", None)
    return redirect(url_for("main"))


if __name__ == '__main__':
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )