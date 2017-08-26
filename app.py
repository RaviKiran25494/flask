from flask import Flask,render_template,flash,redirect,request,url_for,session,logging
# from flask import MySQl
#pip install flask-mysqldb import db
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators#pip install WTForms
# from wtforms.validators import InputRequired,Email,Length
from passlib.hash import sha256_crypt#pip install --user passlib
# from functools import wraps
#scrapy--->pip install scrapy
# spyder---->pip install spyder
#create scrapy file only------>scrapy genspider demo.py https://www.quora.com/How-can-I-write-Python-code-in-HTML
app=Flask(__name__)
# app.config['SECRET_KEY']='Thisissupposedtobesecret!'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'#020201571682 IFSC Code:- ICIC0000202, ICICI BANK LTD, HYDERABAD - PUNJAGUTTA

mysql=MySQL(app)#https://realpython.com/blog/python/the-minimum-viable-test-suite/

@app.route('/')
def home():
	return render_template('home.html')

# @app.route('/login12')
# def login12():
# 	return render_template('login12.html')

@app.route('/about')
def about():
  cur=mysql.connection.cursor()
  cur.execute('''SELECT * FROM users''')
  rv=cur.fetchall()
  return render_template('about.html',rv=rv)

@app.route('/home')
def index():
	cur=mysql.connection.cursor()
	cur.execute('''SELECT * FROM examle''')
	rv=cur.fetchall()
	# return str(rv)

	return render_template('index.html',rv=rv)
@app.route('/home1')
def home1():
	return render_template('home1.py')

@app.route('/login')
def login1():
  return render_template('login.html')

@app.route('/index1')
def index1():
	cur=mysql.connection.cursor()
	cur.execute('''SELECT * FROM examle WHERE id=2''')
	rv=cur.fetchall()
	return str(rv)
@app.route('/index2/<string:insert1>')
def index2(insert1):
	# cur=mysql.connection.cursor()
	# cur.execute('''INSERT INTO `examle`(`id`, `name`, `password`) VALUES (5,'sai','insert1')''')
	# mysql.connection.commit()
	return insert1

@app.route('/update/')
def update():
	cur=mysql.connection.cursor()
	cur.execute('''UPDATE `users` SET `id`=11,`name`='krishana',`password`='krishana123' WHERE id=5''')
	mysql.connection.commit()
	return 'DONE'

@app.route('/update1/<string:insert2>')
def update1(insert2):
	cur=mysql.connection.cursor()
	cur.execute('''SELECT * FROM examle ''')
	rv=cur.fetchall()
	print(insert2)
	# return str(rv)

	return render_template('update1.html',rv=rv)

@app.route('/delete/')
def delete():
	cur=mysql.connection.cursor()
	cur.execute('''DELETE FROM `examle`  WHERE id=7''')
	mysql.connection.commit()
	return 'DELECT SUCCESSFULLY.........'


class RegisterForm(Form):
	name=StringField('Name',[validators.Length(min=1,max=50)])
	username=StringField('Username',[validators.Length(min=4,max=50)])
	email=StringField('Email',[validators.Length(min=6,max=50)])
	password=PasswordField('Password',[
		validators.DataRequired(),
		validators.EqualTo('confirm',message='Passwords do not match')
		])
	confirm=PasswordField('Confirm Password')

@app.route('/register', methods = ['GET', 'POST'])
def register():
   form = RegisterForm(request.form)
   if request.method == 'POST' and form.validate():
       name = form.name.data
       email = form.email.data
       username= form.username.data
       # password = sha256_crypt.hash(str(form.password.data))
       password=form.password.data


       # create cursor
       cur = mysql.connection.cursor()

       cur.execute("INSERT INTO users(name,email,username,password) VALUES(%s, %s, %s, %s)",(name,email,username,password))

       #commit to DB

       mysql.connection.commit()

       #close connection
       cur.close()

       flash('You are now registered and can log in','success')

       return redirect(url_for('login'))

   return render_template('register.html',form = form)

@app.route('/login',methods = ['GET','POST'])
def login():
   if request.method == 'POST':
       #get form fields

       username = request.form['username']
       password_candidate = request.form['password']

       # Create cursor
       cur = mysql.connection.cursor()

       # get user by username

       result = cur.execute("SELECT * FROM users WHERE username = %s",[username])
       print('name:',username)
       if result > 0:

           data = cur.fetchone()
           password = data['password']

           # print('password1',password1);
           print('password:',password_candidate)

           # if sha256_crypt.verify(password_candidate,password):
           if (password_candidate==password):


               #app.logger.info('Passwords Matched')
               session['logged_in'] = True
               session['username'] = username
               # print('password11',password_candidate);
               # print('password12:',password)

               flash('You are now logged in','success')
               return redirect(url_for('about'))
           else:
               error = 'Invalid Login'
               #app.logger.info('Passwords Not matched')
               return render_template('login.html',error=error)
           # close connection
           cur.close()
       else:
           #app.logger.info('No user')
           error:'Username not found'
           return render_template('login.html',error=error)

   return render_template('login.html')
def is_logged_in(f):
   @wraps(f)
   def wrap(*args, **kwargs):
       if 'logged_in' in session:
           return f(*args, **kwargs)
       else:
           flash('Unauthorized, Please Login','danger')
           return redirect(url_for('login'))
   return wrap

   return render_template('login.html')
# Logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out','success')
    return redirect(url_for('login'))

@app.route('/updateprofile')
def updateprofile():
  id=request.args.get('id')
  print('updateproile::',id)
  cur=mysql.connection.cursor()
  cur.execute("SELECT id,name,email FROM users WHERE id=%s",[id])
  rv=cur.fetchall()
  person=rv[0]
  print(person)
  return render_template('update.html',person=person)

@app.route('/updateprofile12')
def updateprofile12():
  name=request.args.get('name')
  email=request.args.get('email')
  
  cur=mysql.connection.cursor()
  cur.execute("SELECT id,name,email FROM users WHERE email=%s",[email])
  rv=cur.fetchall()
  person=rv[0]
  print(person)
  a=person['id']
  print(person['email'])


  cur=mysql.connection.cursor()
  cur.execute("UPDATE `users` SET `name`=%s,`email`=%s WHERE id=%s",[name,email,a])
  print(name)
  print(email)
  print(a)
  mysql.connection.commit()

  return redirect(url_for('about'))

@app.route('/deleteprofile')
def deleteprofile():
  id=request.args.get('id')
  # print("delect",id)
  cur=mysql.connection.cursor()
  cur.execute("DELETE FROM `users`  WHERE id=%s",[id])
  mysql.connection.commit()
 
  return redirect(url_for('about'))


if __name__=='__main__':
  app.secret_key='ravi25494'
  app.run()

