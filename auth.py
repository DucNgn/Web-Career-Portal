from __main__ import app
from flask import flash, request, render_template, url_for, redirect, session
from dbfunctions import verifyAccount, getUserID

@app.before_request
def require_login():
    allowed_routes = ['welcome', 'register', 'login', 'static']
    if request.endpoint not in allowed_routes and 'email' not in session:
        return redirect('/login')

"""
Users ID starting in:
123 - job seeker
312 - employers
999 - admin
"""
@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if verifyAccount(email, password) == 0:
            flash("Something is wrong with your email and password. Please try again!", "warning")
            return redirect(request.url)
        else:
            session["email"] = email
            ID = getUserID(email, password)
            session["ID"] = ID
            tempID = str(ID)
            if tempID[0:3] == '999':
                session["role"] = "Admin"
            elif tempID[0:3] == '312':
                session["role"] = 'Employer'
            elif tempID[0:3] == '123':
                session["role"] = 'Seeker'
            else:
                print("Error: Cannot determine role for session")            
            return redirect('index')
    return render_template("login.html")

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        firstName = request.form['firstname']
        lastName = request.form['lastname']
        email = request.form['email']
        password = request.form['pass']
        return redirect('login')
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.pop("email", None)
    session.pop("ID", None)
    session.pop("role", None)
    return redirect('/')

