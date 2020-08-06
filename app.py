#!/usr/bin/env python
from flask import Flask, url_for, render_template, request, session
#import dbfunctions
import jinja2.exceptions
import secrets
secret_key = secrets.token_hex(16)

app = Flask(__name__)

import auth

@app.route('/')
def index():
    return render_template('index.html')

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
    app.config['SECRET_KEY'] = secret_key
    app.run(debug=True)
