from flask import Flask,render_template,flash,redirect,request,url_for,session,logging
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators#pip install WTForms
from passlib.hash import sha256_crypt#pip install --user passlib
# from functools import wraps

app=Flask(__name__)



app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql=MySQL(app)#https://realpython.com/blog/python/the-minimum-viable-test-suite/

@app.route('/')
def index():
	return render_template("index12.html",title="Signup")

@app.route('/login12')
def login12():
	return render_template("log12.html")
@app.route('/signup',methods=["post"])
def signup():
	username=request.form["username"]
	password=request.form["password"]#INSERT INTO `registers`(`id`, `name`, `password`, `email`) VALUES ([value-1],[value-2],[value-3],[v
	email=request.form["email"]
	cur = mysql.connection.cursor()
	cur.execute("INSERT INTO registers(`name`, `password`, `email`) VALUES(%s, %s, %s)",(username,password,email))
	mysql.connection.commit()
	cur.close()
	return redirect(url_for("login12"))

@app.route('/checkuser',methods=["post"])
def checkuser():
	username=request.form["username"]
	password=request.form["password"]
	cur = mysql.connection.cursor()
	result=cur.execute("SELECT name,password FROM registers where (name='"+username+"' and password='"+password+"')")
	cur.fetchall()
	if (result)>0:
		return 'login successfully....'
	else:
		return redirect(url_for("login12"))

if __name__=='__main__':
  app.secret_key='ravi25494'
  app.run()