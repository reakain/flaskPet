from flask import Flask, redirect, render_template, request, url_for, json
# from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

# mysql = MySQL()

app = Flask(__name__)
app.config["DEBUG"] = True

with open("datab","r") as f:
	temp = f.read().splitlines()
# SQLAlchemy config
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
	username=temp[0],
	password=temp[1],
	hostname=temp[2],
	databasename=temp[3],
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# SQLAlchemy table definitions
class BucketList(db.Model):
	__tablename__ = "BucketList"
	
	user_id = db.Column(db.Integer, primary_key=True)
	user_username = db.Column(db.String(45))
	user_useremail = db.Column(db.String(45))
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
	return render_template('signup.html')
	
@app.route('/signUp',methods=['POST','GET'])
def signUp():
	# create user code will be here !!
	# read the posted values from the UI
	try:
		_name = request.form['inputName']
		_email = request.form['inputEmail']
		_password = request.form['inputPassword']
		
		# validate the received values
		if _name and _email and _password:
			# All Good, let's call MySQL
			_hashed_password = generate_password_hash(_password)
			userinfo = BucketList(content=(_name,_email,_hashed_password))
			exist = BucketList.query.all()
			if _name in exist.user_username:
				return json.dumps({'html':'<span>This username is taken</span>'})
			elif _email in exist.user_useremail:
				return json.dumps({'html':'<span>This e-mail is already in use</span>'})
			else:
				db.session.add(userinfo)
				db.session.commit()
				return json.dumps({'html':'<span>User created successfully!</span>'})

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
		else:
			return json.dumps({'html':'<span>Enter the required fields</span>'})
		
	except Exception as e:
		return json.dumps({'error':str(e)})
	finally:
		cursor.close() 
		conn.close()

		
#if __name__ == "__main__":
#    app.run(ssl_context='adhoc')