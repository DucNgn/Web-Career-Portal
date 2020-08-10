#!/usr/bin/env python
from flask import Flask, url_for, render_template, request, redirect, flash, session
from datetime import date
import dbfunctions
import jinja2.exceptions
import secrets
import os

app = Flask(__name__)

import auth
os.environ['PORT'] = '5000'


@app.route('/index')
def index():
    if session['role'] == "Seeker":
        print("Job seeker signed in")
        userID = session["ID"]

        header1 = "Active job postings"
        numHeader1 = dbfunctions.countActiveJobs()

        header2 = "Monthly fee"
        numHeader2 = dbfunctions.getMonthlyCharge(userID)

        applyCount = dbfunctions.getApplyCount(userID)
        header3 = "You applied to " + str(applyCount) + " positions"
        applyLimit = dbfunctions.getApplyLimit(userID)
        numHeader3 = ""
        percentageHeader3 = 10
        if applyLimit == "unlimited":
            numHeader3 = "Unlimited"
            percentageHeader3 = 0
        elif int(applyLimit) == 0:
            numHeader3 = 0
            percentageHeader3 = 0
        else:
            numHeader3 = int(applyCount) / int(applyLimit) * 100
            numHeader3 = str(numHeader3) + "%"
            percentageHeader3 = numHeader3

        return render_template('index.html', header1 = header1,numHeader1=numHeader1,header2=header2,numHeader2 = numHeader2,header3=header3,numHeader3=numHeader3,percentageHeader3=percentageHeader3 )
    elif session['role'] == "Employer":
        print("Employer signed in")
    elif session['role'] == "Admin":
        print("Admin signed in")
    else:
        print("Error: Cannot identify role")

    return render_template('index.html')

@app.route('/viewUsers')
def viewUsers():
    field_names, results = dbfunctions.getUsers()
    return render_template('viewUsers.html', users = results, usersHeaders = field_names)

@app.route('/viewUsers', methods=['POST'])
def editUsers():
    field_names, results = dbfunctions.getUsers()

    if request.method == 'POST' and "submit-btn" in request.form:

        id = request.form['ID']
        old_id = request.form['old_ID']
        if(id is not old_id):
            dbfunctions.modify_ID(id, old_id)

        firstName= request.form['firstName']
        old_firstName = request.form['old_firstName']
        if(firstName is not old_firstName):
            dbfunctions.modify_firstName(firstName, id)

        lastName= request.form['lastName']
        old_lastName = request.form['old_lastName']
        if(lastName is not old_lastName):
            dbfunctions.modify_lastName(lastName, id)

        title= request.form['title']
        old_title = request.form['old_title']
        if(title is not old_title):
            dbfunctions.modify_title(title, id)

        login_email= request.form['login_email']
        old_login_email = request.form['old_login_email']
        if(login_email is not old_login_email):
            dbfunctions.modify_login_email(login_email, id)

        password= request.form['password']
        old_password = request.form['old_password']
        if(password is not old_password):
            dbfunctions.modify_password(password, id)

        about= request.form['about']
        old_about = request.form['old_about']
        if(about is not old_about):
            dbfunctions.modify_about(about, id)

        account_status= request.form['account_status']
        old_account_status = request.form['old_account_status']
        if(account_status is not old_account_status):
            dbfunctions.modify_account_status(account_status, id)

        category= request.form['category']
        old_category = request.form['old_category']
        if(category is not old_category):
            dbfunctions.modify_category(category, id)

        monthly_charge= request.form['monthly_charge']
        old_monthly_charge = request.form['old_monthly_charge']
        if(monthly_charge is not old_monthly_charge):
            dbfunctions.modify_monthly_charge(monthly_charge, id)

        contact_info= request.form['contact_info']
        old_contact_info = request.form['old_contact_info']
        if(contact_info is not old_contact_info):
            dbfunctions.modify_contact_info(contact_info, id)

        method_of_payment= request.form['method_of_payment']
        old_method_of_payment = request.form['old_method_of_payment']
        if(method_of_payment is not old_method_of_payment):
            dbfunctions.modify_method_of_payment(method_of_payment, id)

        payment_option= request.form['payment_option']
        old_payment_option = request.form['old_payment_option']
        if(payment_option is not old_payment_option):
            dbfunctions.modify_payment_option(payment_option, id)

        balance= request.form['balance']
        old_balance = request.form['old_balance']
        if(balance is not old_balance):
            dbfunctions.modify_balance(balance, id)

        payment_ID= request.form['payment_ID']
        old_payment_ID = request.form['old_payment_ID']
        if(payment_ID is not old_payment_ID):
            dbfunctions.modify_payment_ID(payment_ID, id)

        return redirect(url_for('viewUsers'))
    if request.method == 'POST' and "delete-btn" in request.form:
        id = request.form['hidden-id']
        dbfunctions.deleteUser(id)
        return redirect(url_for('viewUsers'))


    return redirect(url_for('viewUsers'))

@app.route('/viewJobs')
def viewJobs():
    field_names, results = dbfunctions.getJobs()
    return render_template('viewJobs.html', jobs = results, jobsHeaders = field_names)

@app.route('/postJobs', methods=['POST'])
def postJob():
    if(request.form is not None):
        job_title = request.form['jobTitle']
        dbfunctions.postJob(job_title)
        return render_template('postJobs.html',message="Success, job has been created!")
    return render_template('postJobs.html')

@app.route('/applyJob', methods=['POST'])
def applyJob():
    if(request.form is not None):
        jobSeekerID = request.form['jobSeekerID']
        jobID = request.form['jobID']
        appliedDate = date.today().strftime("%Y-%m-%d")
        coverLetter = 'coverletter path'
        resume = 'resume path'
    dbfunctions.applyJob(jobSeekerID, jobID, appliedDate, coverLetter, resume)
    flash('Job applied successfully!')
    return redirect(url_for('viewJobs'))

@app.errorhandler(jinja2.exceptions.TemplateNotFound)
def template_not_found(e):
    return not_found(e)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

@app.route('/<pagename>')
def admin(pagename):
    return render_template(pagename+'.html')

if __name__ == '__main__':
    secret_key = secrets.token_hex(16)
    app.config['SECRET_KEY'] = secret_key
    port = int(os.environ['PORT'])
    app.run(debug=True, host='0.0.0.0', port = port)
