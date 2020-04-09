import pandas as pd
import requests
import zillow
# import pprint as pp
import json
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect


# Create an instance of Flask
app = Flask(__name__)

connection_string = "postgres:apartment@homeslice.cjnrjw08kldx.us-east-2.rds.amazonaws.com:5432/HomeSliceDB"
engine = create_engine(f'postgresql://{connection_string}')
api = zillow.ValuationApi()
key = "X1-ZWz17fdl35adqj_3bebs"

def address_search(address, postal_code):
    request_data = api.GetSearchResults(key, address, postal_code)
    result = request_data.get_dict()
    address = result['full_address']
    
    zestimate = result['zestimate']
    comb_dict = dict(zestimate)
    comb_dict.update(address)
    combined_df = pd.DataFrame.from_dict(comb_dict, orient='index').T

    combined_df['risk_adj_value'] = (combined_df['amount']*.85) #Risk adjusting home by 15%, reducing home val by 15%
    combined_df['max_cash_limit'] = combined_df['risk_adj_value']*.30 #Cannot buy more than 30% of someones home equity, bc then youre pushing majority ownership
    combined_df.to_sql(name='zillow', con=engine, if_exists='append', index=False)
    # zestimate_amount = combined_df["amount"]
    # max_cash_offer = combined_df["max_cash_limit"]
    # html_table = combined_df.to_html()

    
    return(combined_df)
            

@app.route('/',methods = ['GET', 'POST'])
def zillow():
    if request.method == "POST":
        address = request.form['address']
        postal_code = request.form['zipcode']
        print(address)
        print(postal_code)
        #Function to call data from Zillow, return dataframe and append to master DB table
        address_search(address,postal_code)
        

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)