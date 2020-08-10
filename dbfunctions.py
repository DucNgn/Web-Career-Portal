import sshtunnel
import pymysql
import config
import random

sshtunnel.SSH_TIMEOUT = 30000

# Connecting to database

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

# sql = "SELECT * FROM admin;"

# try:
#     # Execute the SQL command
#     cursor.execute(sql)
#     # Fetch all the rows in a list of lists.
#     results = cursor.fetchall()
#     # for item in results:
#     #     print(item)
# except:
#     print("Error: unable to fetch data")

# db.close()

def getUsers():
    sql = "SELECT * FROM user ;"

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

    return field_names, results




def modify_ID(id, old_id):
    sql = "UPDATE user set ID=\'"+id+"\' WHERE ID=\'"+old_id+"\';"
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print("Problem updating ID into db: " + str(e))
        return False

def modify_firstName(firstName, ID):
    sql = "UPDATE user set firstName=\'"+firstName+"\' WHERE ID=\'"+ID+"\';"
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print("Problem updating firstName into db: " + str(e))
        return False

def modify_lastName(lastName, ID):
    sql = "UPDATE user set lastName=\'"+lastName+"\' WHERE ID=\'"+ID+"\';"
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print("Problem updating lastName into db: " + str(e))
        return False


def modify_title(title, ID):
    sql = "UPDATE user set title=\'"+title+"\' WHERE ID=\'"+ID+"\';"
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print("Problem updating title into db: " + str(e))
        return False

def modify_login_email(login_email, ID):
    sql = "UPDATE user set login_email=\'"+login_email+"\' WHERE ID=\'"+ID+"\';"
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print("Problem updating login_email into db: " + str(e))
        return False

def modify_password(password, ID):
    sql = "UPDATE user set password=\'"+password+"\' WHERE ID=\'"+ID+"\';"
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print("Problem updating password into db: " + str(e))
        return False

def modify_about(about, ID):
    sql = "UPDATE user set about=\'"+about+"\' WHERE ID=\'"+ID+"\';"
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print("Problem updating about into db: " + str(e))
        return False


def modify_account_status(account_status, ID):
    sql = "UPDATE user set account_status=\'"+account_status+"\' WHERE ID=\'"+ID+"\';"
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print("Problem updating account_status into db: " + str(e))
        return False

def modify_category(category, ID):
    sql = "UPDATE user set category=\'"+category+"\' WHERE ID=\'"+ID+"\';"
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print("Problem updating category into db: " + str(e))
        return False


def modify_monthly_charge(monthly_charge, ID):
    sql = "UPDATE user set monthly_charge=\'"+monthly_charge+"\' WHERE ID=\'"+ID+"\';"
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print("Problem updating monthly_charge into db: " + str(e))
        return False

def modify_contact_info(contact_info, ID):
    sql = "UPDATE user set contact_info=\'"+contact_info+"\' WHERE ID=\'"+ID+"\';"
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print("Problem updating contact_info into db: " + str(e))
        return False


def modify_method_of_payment(method_of_payment, ID):
    sql = "UPDATE user set method_of_payment=\'"+method_of_payment+"\' WHERE ID=\'"+ID+"\';"
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print("Problem updating method_of_payment into db: " + str(e))
        return False

def modify_payment_option(payment_option, ID):
    sql = "UPDATE user set payment_option=\'"+payment_option+"\' WHERE ID=\'"+ID+"\';"
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print("Problem updating payment_option into db: " + str(e))
        return False

def modify_balance(balance, ID):
    sql = "UPDATE user set balance=\'"+balance+"\' WHERE ID=\'"+ID+"\';"
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print("Problem updating balance into db: " + str(e))
        return False


def modify_payment_ID(payment_ID, ID):
    sql = "UPDATE user set payment_ID=\'"+payment_ID+"\' WHERE ID=\'"+ID+"\';"
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print("Problem updating payment_ID into db: " + str(e))
        return False




def deleteUser(ID):
    sql= "DELETE from user where id=\'"+ID+"\';"

    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print("Problem deleting \'"+ID+"\' from db: " + str(e))
        return False

def getJobs():
    sql = "SELECT * FROM jobs ;"

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

    return field_names, results

def postJob(job_title):
    sql = "INSERT INTO jobs(job_title) VALUES(\'"+job_title+"\');"

    # print(sql)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit SQL command
        db.commit()
        return True
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return False

def verifyAccount(email, password):
    email.replace(" ", "")
    password.replace(" ", "")
    sqlUser= "SELECT EXISTS (SELECT * FROM user WHERE login_email=\'"+email+"\' AND password=\'"+password+"\')"
    sqlAdmin = "SELECT EXISTS (SELECT * FROM admin WHERE login_email=\'"+email+"\' AND password=\'"+password+"\')"

    try:
        cursor.execute(sqlUser)
        result = cursor.fetchall()
        if result[0][0] == 0:
            cursor.execute(sqlAdmin)
            result = cursor.fetchall()
        return result[0][0]
    except Exception as e:
        print("Problem verifying user info: " + str(e))
        return False

def isBannedAcc(email):
    sql ="SELECT account_status FROM user WHERE login_email = \'"+email+"\';"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        if result[0][0] == "banned":
            return True
        else:
            return False
    except Exception as e:
        print("Problem verifying if user is banned. Info: " + str(e))
        return False


def emailExisted(email):
    email.replace(" ", "")
    sqlUser= "SELECT EXISTS (SELECT * FROM user WHERE login_email=\'"+email+"\')"
    sqlAdmin = "SELECT EXISTS (SELECT * FROM admin WHERE login_email=\'"+email+"\')"
    try:
        cursor.execute(sqlUser)
        result = cursor.fetchall()
        if result[0][0] == 0:
            cursor.execute(sqlAdmin)
            result = cursor.fetchall()
        return bool(result[0][0])
    except Exception as e:
        print("Problem verifying user email " + str(e))
        return False

def getUserID(email, password):
    sql = "SELECT ID FROM user WHERE login_email=\'"+email+"\' AND password=\'"+password+"\'"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:
            return result[0][0]
        else:
            sqlAdmin ="SELECT ID FROM admin WHERE login_email=\'"+email+"\' AND password=\'"+password+"\'"
            cursor.execute(sqlAdmin)
            result = cursor.fetchall()
        return result[0][0]
    except Exception as e:
        print("Problem getting user ID: " + str(e))
        return False

def registerUser(firstName, lastName, title, email, password, role):
    userID = str(createID(role))
    password = str(password)
    userSql = "INSERT INTO user(ID, firstName, lastName, title, login_email, password, account_status) VALUES (\'"+userID+"\', \'"+firstName+"\', \'"+lastName+"\', \'"+title+"\', \'"+email+"\', \'"+password+"\', \'active\');"
    seekerSql = "INSERT INTO jobSeeker(ID, applyLimit) VALUES (\'"+userID+"\', \'"+str(0)+"\') "
    employerSql = "INSERT INTO employer(ID, posting_count, postingLimit) VALUES (\'"+userID+"\', \'"+str(0)+"\' , \'"+str(0)+"\') "
    try:
        cursor.execute(userSql)
        if role =="employer":
            cursor.execute(employerSql)
        else:
            cursor.execute(seekerSql)
        db.commit()
        return True
    except Exception as e:
        print("Problem while registering new user to the system: " + str(e))
        return False

def createID(role):
    prefix = 123
    if role == "employer":
        prefix = 312
    while True:
        sampleID = str(prefix) + str(random.randint(0000, 9999))
        if not isDuplicatedUID(sampleID):
            return sampleID

def isDuplicatedUID(sampleID):
    sql= "SELECT EXISTS (SELECT * FROM user WHERE ID=\'"+sampleID+"\')"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        return bool(result[0][0])
    except Exception as e:
        print("Problem checking for duplicated user ID " + str(e))
        return False


def applyJob(jobSeekerID, jobID, appliedDate, coverLetter, resume):
    # sql = "INSERT INTO applyTo VALUES(\'1231221\',\'1232112\',\'2020-02-02\',\'pending\',\'coverletter\',\'resume\');"
    sql = "INSERT INTO applyTo VALUES(\'"+jobSeekerID+"\',\'"+jobID+"\',\'"+appliedDate+"\',\'pending\',\'"+coverLetter+"\',\'"+resume+"\');"

    print(sql)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit SQL command
        db.commit()
        return True
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return False

def countActiveJobs():
    sql = "SELECT COUNT(*) FROM jobs WHERE job_status=\"active\""
    return count(sql)

def getMonthlyCharge(ID):
    sql = "SELECT monthly_charge FROM user WHERE ID=" + str(ID)
    return count(sql)

def getApplyCount(ID):
    sql = "SELECT apply_count FROM jobSeeker WHERE ID=" + str(ID)
    return count(sql)

def getApplyLimit(ID):
    sql = "SELECT applyLimit FROM jobSeeker WHERE ID=" + str(ID)
    return count(sql)

def count(query):
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]
    except Exception as e:
        print("Problem in counting: query: " + query + str(e))
