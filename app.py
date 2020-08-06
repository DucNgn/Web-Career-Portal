#!/usr/bin/env python
from flask import Flask, url_for, render_template
import sshtunnel
import pymysql
import config
import jinja2.exceptions

sshtunnel.SSH_TIMEOUT = 30000

server = sshtunnel.SSHTunnelForwarder(
    'login.encs.concordia.ca',
    ssh_username=config.SSH_USERNAME,
    ssh_password=config.SSH_PASSWORD,
    remote_bind_address=('qxc353.encs.concordia.ca', 3306)
)

server.start()
print(server.local_bind_port)

print("Connected to server")

db = pymysql.connect(
    host="localhost", 
    port=server.local_bind_port,
    user=config.DB_USER, 
    password=config.DB_PASSWORD,
    database=config.DB_DATABASE,
    connect_timeout=3100)

cursor = db.cursor()

print("Connected to database")

sql = "SELECT * FROM admin;"

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    # for item in results:
    #     print(item)
except:
    print("Error: unable to fetch data")

# db.close()

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<pagename>')
def admin(pagename):
    return render_template(pagename+'.html')

@app.route('/viewJobs')
def viewJobs():
    sql = "SELECT * FROM jobs;"

    results = []
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        # for item in results:
        #     print(item)
    except:
        print("Error: unable to fetch data")

    # Table headers
    field_names = [i[0] for i in cursor.description]

    return render_template('viewJobs.html', jobs = results, jobsHeaders = field_names)

@app.errorhandler(jinja2.exceptions.TemplateNotFound)
def template_not_found(e):
    return not_found(e)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)
