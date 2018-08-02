from flask import Flask, redirect, render_template, request, url_for, json
# from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

# mysql = MySQL()

app = Flask(__name__)
app.config["DEBUG"] = True

# SQLAlchemy config
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="<the username from the 'Databases' tab>",
    password="<the password you set on the 'Databases' tab>",
    hostname="<the database host address from the 'Databases' tab>",
    databasename="<the database name you chose, probably yourusername$comments>",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# SQLAlchemy table definitions
class BucketList(db.Model):
	__tablename__ = "BucketList"
	
	user_id = db.Column(db.Integer, primary_key=True)
	user_name = db.Column(db.String(45))
	user_username = db.Column(db.String(45))
	user_password = db.Column(db.String(45))

# MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'jay'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'jay'
# app.config['MYSQL_DATABASE_DB'] = 'BucketList'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)

@app.route('/')
def index():
	return render_template('main_page.html')

@app.route('/showSignUp')
def showSignUp():
	return 'render_template('signup.html')
	
# @app.route('/signUp',methods=['POST','GET'])
# def signUp():
    # # create user code will be here !!
	# # read the posted values from the UI
	# try:
		# _name = request.form['inputName']
		# _email = request.form['inputEmail']
		# _password = request.form['inputPassword']
		
		# # validate the received values
		# if _name and _email and _password:
			# # All Good, let's call MySQL
				
				# conn = mysql.connect()
				# cursor = conn.cursor()
				# _hashed_password = generate_password_hash(_password)
				# cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
				# data = cursor.fetchall()

				# if len(data) is 0:
					# conn.commit()
					# return json.dumps({'message':'User created successfully !'})
				# else:
					# return json.dumps({'error':str(data[0])})
		# else:
			# return json.dumps({'html':'<span>Enter the required fields</span>'})
		
	# except Exception as e:
        # return json.dumps({'error':str(e)})
    # finally:
        # cursor.close() 
        # conn.close()
