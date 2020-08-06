#!/usr/bin/env python
from flask import Flask, url_for, render_template
import dbfunctions
import jinja2.exceptions

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<pagename>')
def admin(pagename):
    return render_template(pagename+'.html')

@app.route('/viewJobs')
def viewJobs():
    field_names, results = dbfunctions.getJobs()

    return render_template('viewJobs.html', jobs = results, jobsHeaders = field_names)

@app.errorhandler(jinja2.exceptions.TemplateNotFound)
def template_not_found(e):
    return not_found(e)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)
