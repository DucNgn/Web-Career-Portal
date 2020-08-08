from __main__ import app
from flask import flash, request, render_template, url_for, redirect, session
from dbfunctions import verifyAccount, getUserID, emailExisted, registerUser

@app.before_request
def require_login():
    allowed_routes = ['welcome', 'register', 'login', 'static', 'forgotPassword']
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
        title = request.form.get('title')
        email = request.form['email']
        password = request.form['pass']
        role = request.form.get('role')
        print('Done getting info from the form')
        if emailExisted(email):
            flash("Your email is already registered in our system. Please log in instead", "warning")
            return redirect(request.url)
        else:
            if registerUser(firstName, lastName, title, email, password, role):
                flash("Registered successfully, login to get started", "success")
                return redirect(request.url)                
            else:
                flash("An unexpected problem occurred, please try again", "warning")
                return redirect(request.url) 
    else:
        return render_template("register.html")

@app.route("/forgotPassword", methods=['POST', 'GET'])
def forgotPassword():
    if request.method == 'POST':
        email = request.form['email']
        if emailExisted(email):
            flash("Please check your email for a code to reset password", "success")
            # Sending email and retrieve code here
            return redirect(request.url)
        else:
            flash("Your email is not registered in our system", "warning")
            return redirect(request.url)
    return render_template("forgotPassword.html")

@app.route("/logout")
def logout():
    session.pop("email", None)
    session.pop("ID", None)
    session.pop("role", None)
    return redirect('/')

