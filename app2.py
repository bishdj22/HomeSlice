# import pandas as pd
# import requests
# import zillow
# # import pprint as pp
# import json
# from sqlalchemy import create_engine
# from flask import Flask, jsonify, render_template,request
# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask, render_template, redirect
# from calculations import address_search
# from config import zillow_key, database_key
# from flask_wtf import FlaskForm 
# from wtforms import StringField, PasswordField, BooleanField,IntegerField
# from wtforms.validators import InputRequired, Email, Length
# from flask_bootstrap import Bootstrap
# from sqlalchemy.ext.automap import automap_base


# # Create an instance of Flask
# app = Flask(__name__)

# connection_string = database_key
# engine = create_engine(f'postgresql://{connection_string}')

# conn=engine.connect()

# print(conn.execute("select count(*) from zillow"))
# api = zillow.ValuationApi()
# key = "X1-ZWz17fdl35adqj_3bebs"
# key = zillow_key
# app.config['SECRET_KEY'] = 'awssecreykey123'
# db = SQLAlchemy(app)
# bootstrap = Bootstrap(app)

# firstname = None
# lastname = None
# social_security = None
# phone_number = None
# gender = None
# address = None
# postal_code = None
# email = None
# password = None
            

# @app.route('/',methods = ['GET', 'POST'])
# def zillow_call():
#     #Default results
#     results = ('435,000', '17,000')
#     print(request.method)
#     if request.method == "POST":
#         #Passing user inputs from HTML to python variable
#         address = request.form['address']
#         postal_code = request.form['zipcode']
#         print(address)
#         print(postal_code)

#         #Function to call data from Zillow and return data
#         results = address_search(address,postal_code)
        

#     return render_template('index.html', data=results)

# ########Signup Froms 
# # class RegisterForm(FlaskForm):
# #     name = StringField('name', validators=[InputRequired(), Length(max=50)])
# #     address = StringField('address', validators=[InputRequired(), Length(min=1, max=8)])
# #     socialsecurity = StringField('socialsecurity', validators=[InputRequired(), Length(min=1, max=8)])
# #     email = StringField('email', validators=[InputRequired(), Length(min=1, max=8)])
# #     phonenumber = IntegerField('phonenumber', validators=[InputRequired(), Length(min=1, max=8)])
# #     gender = StringField('gender', validators=[InputRequired(), Length(min=1, max=8)])


# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     print("working...")
#     #Default results
#     print(request.method)
#     # results = ('435,000', '17,000')
#     if request.method == "POST":
#         global firstname 
#         global lastname
#         global social_security
#         global phone_number
#         global gender
#         global address
#         global postal_code
#         global email
#         global password 

#         firstname = request.form['first-name']
#         lastname = request.form['last-name']
#         social_security = request.form['social-security']
#         phone_number = request.form['phone-number']
#         gender = request.form['gender']
#         address = request.form['address']
#         postal_code = request.form['zipcode']
#         email = request.form['email']
#         password = request.form['password'] 

#         #Passing user inputs from HTML to python variable
#         user_dict = {'first-name': firstname, 'last-name' : lastname, 'social-security': social_security, 'phone-number': phone_number, 'gender': gender, 'address': address, 'zipcode': postal_code, 'gender': gender, 'email': email, 'password': password}

#         print(firstname)
#         print(lastname)
#         print(social_security)
#         print(phone_number)
#         print(gender)
#         print(address)
#         print(postal_code)
#         print(email)
#         print(password)

#         user_df = pd.DataFrame.from_dict(user_dict, orient='index').T
#         user_df['time_stamp'] = pd.Timestamp.now()
        
#         user_df.to_sql(name='user_data', con=engine, if_exists='append', index=False)

#         return redirect('/welcome', code=302)
        
#     return render_template('signup.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     print("working...")
#     #Default results
#     print(request.method)
#     return render_template('login.html')



# @app.route('/test', methods = ['GET', 'POST'])
# def zillow_call1():
#     print("working...")
#     #Default results
#     print(request.method)
#     results = ('435,000', '17,000')
#     if request.method == "POST":
#         #Passing user inputs from HTML to python variable
#         address = request.form['address']
#         postal_code = request.form['zipcode']
#         print(address)
#         print(postal_code)

#         #Function to call data from Zillow and return data
#         results = address_search(address,postal_code)  

#     return render_template('index.html', data=results)

# @app.route("/about")
# def about():
#     print('Under Construction')
#     return render_template('about.html')

# @app.route("/dash")
# def dashboard():
#     print('Under Construction')
#     return render_template('dashboard.html')

# @app.route("/contact")
# def contact():
#     print('Under Construction')
#     return render_template('contact.html')

# @app.route("/welcome")
# def welcome():
#     print('Under Construction')
#     name = firstname

#     return render_template('welcome.html',say=name)

# if __name__ == "__main__":
#     app.run(debug=True)

# @app.route('/signup1', methods=['GET', 'POST'])
# def signup():
#     print("working...")
#     #Default results
#     print(request.method)
#     # results = ('435,000', '17,000')
#     if request.method == "POST":
#         global firstname 
#         global lastname
#         global social_security
#         global phone_number
#         global gender
#         global address
#         global postal_code
#         global email
#         global password 

#         firstname = request.form['first-name']
#         lastname = request.form['last-name']
#         social_security = request.form['social-security']
#         phone_number = request.form['phone-number']
#         gender = request.form['gender']
#         address = request.form['address']
#         postal_code = request.form['zipcode']
#         email = request.form['email']
#         password = request.form['password'] 

#         #Passing user inputs from HTML to python variable
#         user_dict = {'first-name': firstname, 'last-name' : lastname, 'social-security': social_security, 'phone-number': phone_number, 'gender': gender, 'address': address, 'zipcode': postal_code, 'gender': gender, 'email': email, 'password': password}

#         print(firstname)
#         print(lastname)
#         print(social_security)
#         print(phone_number)
#         print(gender)
#         print(address)
#         print(postal_code)
#         print(email)
#         print(password)

#         user_df = pd.DataFrame.from_dict(user_dict, orient='index').T
#         user_df['time_stamp'] = pd.Timestamp.now()
        
#         user_df.to_sql(name='user_data', con=engine, if_exists='append', index=False)

#         return redirect('/welcome', code=302)
        
#     return render_template('signup.html')

# @app.route('/login1', methods=['GET', 'POST'])
# def login():
#     print("working...")
#     #Default results
#     print(request.method)
#     return render_template('login.html')

import pandas as pd
import requests
import zillow
# import pprint as pp
import json
from datetime import datetime
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template,request,redirect, url_for,request,flash,session,g
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect
from calculations import address_search
from config import zillow_key, database_key
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField,IntegerField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap
from sqlalchemy.ext.automap import automap_base
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import INTERVAL
from sqlalchemy.sql.functions import concat
from datetime import datetime, timedelta


# Create an instance of Flask
app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] ='postgres:apartment@homeslice.cjnrjw08kldx.us-east-2.rds.amazonaws.com:5432/HomeSliceDB'
connection_string = database_key
engine = create_engine(f'postgresql://{connection_string}')



conn=engine.connect()

print(conn.execute("select count(*) from zillow"))
api = zillow.ValuationApi()
key = "X1-ZWz17fdl35adqj_3bebs"
key = zillow_key
app.config['SECRET_KEY'] = 'awssecreykey123'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:apartment@homeslice.cjnrjw08kldx.us-east-2.rds.amazonaws.com:5432/HomeSliceDB"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


firstname = None
lastname = None
social_security = None
phone_number = None
gender = None
address = None
postal_code = None
email = None
password = None
            

@app.route('/',methods = ['GET', 'POST'])
def zillow_call():
    #Default results
    results = ('435,000', '17,000')
    print(request.method)
    if request.method == "POST":
        #Passing user inputs from HTML to python variable
        address = request.form['address']
        postal_code = request.form['zipcode']
        print(address)
        print(postal_code)

        #Function to call data from Zillow and return data
        results = address_search(address,postal_code)
        

    return render_template('index.html', data=results)


# @app.route('/signup1', methods=['GET', 'POST'])
# def signup():
#     print("working...")
#     #Default results
#     print(request.method)
#     # results = ('435,000', '17,000')
#     if request.method == "POST":
#         global firstname 
#         global lastname
#         global social_security
#         global phone_number
#         global gender
#         global address
#         global postal_code
#         global email
#         global password 

#         firstname = request.form['first-name']
#         lastname = request.form['last-name']
#         social_security = request.form['social-security']
#         phone_number = request.form['phone-number']
#         gender = request.form['gender']
#         address = request.form['address']
#         postal_code = request.form['zipcode']
#         email = request.form['email']
#         password = request.form['password'] 

#         #Passing user inputs from HTML to python variable
#         user_dict = {'first-name': firstname, 'last-name' : lastname, 'social-security': social_security, 'phone-number': phone_number, 'gender': gender, 'address': address, 'zipcode': postal_code, 'gender': gender, 'email': email, 'password': password}

#         print(firstname)
#         print(lastname)
#         print(social_security)
#         print(phone_number)
#         print(gender)
#         print(address)
#         print(postal_code)
#         print(email)
#         print(password)

#         user_df = pd.DataFrame.from_dict(user_dict, orient='index').T
#         user_df['time_stamp'] = pd.Timestamp.now()
        
#         user_df.to_sql(name='user_data', con=engine, if_exists='append', index=False)

#         return redirect('/welcome', code=302)
        
#     return render_template('signup.html')

# @app.route('/login1', methods=['GET', 'POST'])
# def login():
#     print("working...")
#     #Default results
#     print(request.method)
#     return render_template('login.html')



@app.route('/test', methods = ['GET', 'POST'])
def zillow_call1():
    print("working...")
    #Default results
    print(request.method)
    results = ('435,000', '17,000')
    if request.method == "POST":
        #Passing user inputs from HTML to python variable
        address = request.form['address']
        postal_code = request.form['zipcode']
        print(address)
        print(postal_code)

        #Function to call data from Zillow and return data
        results = address_search(address,postal_code)  

    return render_template('index.html', data=results)

@app.route("/about")
def about():
    print('Under Construction')
    return render_template('about.html')

@app.route("/dash")
def dashboard():
    print('Under Construction')
    return render_template('dashboard.html')

@app.route("/contact")
def contact():
    print('Under Construction')
    return render_template('contact.html')

@app.route("/welcome")
def welcome():
    print('Under Construction')
    name = firstname

    return render_template('welcome.html',say=name)
@app.route("/test1")
def test():
    return render_template('test.html')
@app.route("/account")
def account():
    return render_template('account-creation.html')

@app.route("/seller")
def seller():
    return render_template('seller.html')
    ##########Login Attempt 

@login_manager.user_loader
# identifing users that are logged in
def load_user(user_id):
    return Profile.query.get(int(user_id))

class Profile(UserMixin, db.Model):
    __tablename__ = "profile"
    id = db.Column('user_id',db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    registered_on = db.Column('registered_on' , db.DateTime)
    account = db.relationship('Account' , backref='profile',lazy='dynamic')
    def __init__(self , username ,password , email):

        self.username = username

        self.password = password

        self.email = email

        self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.id)
    def __repr__(self):
        return '<User %r>' % (self.username)


class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column('account_id', db.Integer, primary_key=True)
    address = db.Column(db.String(120))
    phone = db.Column(db.String)
    dob = db.Column(db.DateTime)
    social = db.Column(db.Integer)
    gender = db.Column(db.String)
    registered_on = db.Column('registered_on' , db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('profile.user_id'))

    def __init__(self, address, phone,dob,social,gender):
        self.address = address
        self.phone = phone
        self.dob = dob
        self.social = social
        self.gender = gender
        self.registered_on = datetime.utcnow()


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        print(username)
        if not (username and password):
            flash("Username or Password cannot be empty")
        else:
            username = username.strip()
            password = password.strip()
        hashed_pwd = generate_password_hash(password, 'sha256')
        new_user = Profile(username=username, password=hashed_pwd,email=email)
        db.session.add(new_user)
        try:
            db.session.commit()
            # flash("User account has been created.")
            return redirect(url_for("login"))
        except:
            flash("Username {u} is not available.".format(u=username))
            return redirect(url_for("signup"))
    return render_template('signup.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        if not (email and password):
            flash("Username or Password cannot be empty.")
            # return redirect(url_for('login'))
        else:
            email = email.strip()
            password = password.strip()

        user = Profile.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            now = datetime.now()
            five_min = now - timedelta(minutes=5)

            login_user(user)
            session[email] = True
            # if user.query.filter(user.registered_on > five_min).filter(user.registered_on < now).all():
            if user.query.filter(user.registered_on < five_min).all():
            # return redirect(url_for("account"))
                print("nada")
                return redirect(url_for("seller"))
                
            elif user.query.filter(user.registered_on > five_min).all():
                print("collins")
                return redirect(url_for("account"))
            else:
                return None
        else:
            flash("Invalid username or password.")

        # return redirect("account-creation.html")

    return render_template("login.html")


@login_required
@app.route('/account', methods = ['GET' , 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['address']:
            flash('address is required', 'error')
        else:
            account = Account(request.form['address'], request.form['phone'],request.form['dob'],request.form['social'],request.form['gender'])
            account.user_id = g.user.id
            db.session.add(account)
            db.session.commit()
            flash('Account item was successfully created')
        return redirect(url_for("seller"))
    return render_template('seller.html')

@app.before_request
def before_request():
    g.user = current_user

@app.route('/logout')

def logout():

    logout_user()

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)


