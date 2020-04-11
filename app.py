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



# Create an instance of Flask
app = Flask(__name__)

connection_string = database_key
engine = create_engine(f'postgresql://{connection_string}')
api = zillow.ValuationApi()
# key = "X1-ZWz17fdl35adqj_3bebs"
key = zillow_key
db = SQLAlchemy(app)

            

@app.route('/',methods = ['GET', 'POST'])
def zillow_call():
    #Default results
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
########Signup Froms 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(50))
    socialsecurity = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phonenumber = db.Column(db.Integer)
    gender = db.Column(db.String(50))
  


class RegisterForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Length(max=50)])
    username = StringField('address', validators=[InputRequired(), Length(min=1, max=8)])
    socialsecurity = StringField('socialsecurity', validators=[InputRequired(), Length(min=1, max=8)])
    email = StringField('email', validators=[InputRequired(), Length(min=1, max=8)])
    phonenumber = IntegerField('phonenumber', validators=[InputRequired(), Length(min=1, max=8)])
    gender = StringField('gender', validators=[InputRequired(), Length(min=1, max=8)])


@app.route('/', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(name=form.name.data, username=form.username.data,socialsecurity=form.socialsecurity.data,email=form.email.data,phonenumber=form.phonenumber.data,gender=form.gender.data)
        db.session.add(new_user)
        db.session.commit()
        return '<h1>New user has been created!</h1>'
        return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)