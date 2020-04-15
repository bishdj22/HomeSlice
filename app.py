import pandas as pd
import requests
import zillow
# import pprint as pp
import json
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect
from calculations import address_search
from config import zillow_key, database_key
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField,IntegerField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap
from sqlalchemy.ext.automap import automap_base


# Create an instance of Flask
app = Flask(__name__)

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

########Signup Froms 
class RegisterForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Length(max=50)])
    address = StringField('address', validators=[InputRequired(), Length(min=1, max=8)])
    socialsecurity = StringField('socialsecurity', validators=[InputRequired(), Length(min=1, max=8)])
    email = StringField('email', validators=[InputRequired(), Length(min=1, max=8)])
    phonenumber = IntegerField('phonenumber', validators=[InputRequired(), Length(min=1, max=8)])
    gender = StringField('gender', validators=[InputRequired(), Length(min=1, max=8)])

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    print("working...")
    #Default results
    print(request.method)
    # results = ('435,000', '17,000')
    if request.method == "POST":
        firstname = request.form['first-name']
        lastname = request.form['last-name']
        social_security = request.form['social-security']
        phone_number = request.form['phone-number']
        gender = request.form['gender']
        address = request.form['address']
        postal_code = request.form['zipcode']
        email = request.form['email']
        password = request.form['password'] 

        #Passing user inputs from HTML to python variable
        user_dict = {'first-name': firstname, 'last-name' : lastname, 'social-security': social_security, 'phone-number': phone_number, 'gender': gender, 'address': address, 'zipcode': postal_code, 'gender': gender, 'email': email, 'password': password}

        print(firstname)
        print(lastname)
        print(social_security)
        print(phone_number)
        print(gender)
        print(address)
        print(postal_code)
        print(email)
        print(password)

        user_df = pd.DataFrame.from_dict(user_dict, orient='index').T
        user_df.to_sql(name='user_data', con=engine, if_exists='append', index=False)

        def result_getter():
            connection = engine.connect()
            query = "select first-name from user_data where first-name = " + firstname + ";"
            result = connection.execute(query)
            for i in result:
                results = i
            return results
            results = result_getter(firstname)
            print("query finished")
            print(results)
            print("Success")

        
        
    return render_template('signup.html')


# @app.route('/signup1', methods=['GET', 'POST'])
# def signup():
#     form = RegisterForm()
#     if request.method == 'POST': 
#         # new_user = User(name=form.name.data, address=form.address.data,socialsecurity=form.socialsecurity.data,email=form.email.data,phonenumber=form.phonenumber.data,gender=form.gender.data)
#         user_dict = {'name':form.name.data, 'address': form.address.data,'socialsecurity': form.socialsecurity.data, 'email': form.email.data, 'phonenumber': form.phonenumber.data, 'gender': form.gender.data}
#         user_df = pd.DataFrame.from_dict(user_dict, orient='index').T
#         user_df.to_sql(name='user_data', con=engine, if_exists='append', index=False)

#     return render_template('signup.html', form=form)



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


if __name__ == "__main__":
    app.run(debug=True)