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


# Create an instance of Flask
app = Flask(__name__)

connection_string = database_key
engine = create_engine(f'postgresql://{connection_string}')
api = zillow.ValuationApi()
# key = "X1-ZWz17fdl35adqj_3bebs"
key = zillow_key

            

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


if __name__ == "__main__":
    app.run(debug=True)