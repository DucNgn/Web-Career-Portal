from __main__ import app
from flask import flash, request, render_template, url_for, redirect, session
from dbfunctions import verifyAccount, getUserID

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
            if str(ID)[0:2] == '999':
                session["role"] = "Admin"
            elif str(ID)[0:2] == '312':
                session["role"] = 'Employer'
            elif str(ID)[0:2] == '123':
                session["role"] = 'Seeker'
            else:
                print("error")            
            return redirect('index')
    return render_template("login.html")
