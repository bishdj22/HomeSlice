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


# Create an instance of Flask
app = Flask(__name__)

connection_string = "postgres:apartment@homeslice.cjnrjw08kldx.us-east-2.rds.amazonaws.com:5432/HomeSliceDB"
engine = create_engine(f'postgresql://{connection_string}')
api = zillow.ValuationApi()
key = "X1-ZWz17fdl35adqj_3bebs"

            

@app.route('/',methods = ['GET', 'POST'])
def zillow():
    if request.method == "POST":
        address = request.form['address']
        postal_code = request.form['zipcode']
        # address1 = (f'{address}')
        # postal_code1 = (f'{postal_code}')
        print(address)
        print(postal_code)
        address_search(address,postal_code)
        #Function to call data from Zillow and return dataframe

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)