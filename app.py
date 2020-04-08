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


@app.route('/',methods = ['GET', 'POST'])
def zillow():
    if request.method == "POST":
         address = request.form['address']
         postal = request.form['Zip Code']
         print(address)
         print(postal)
         #Function to call data from Zillow and return dataframe

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
    
        return(combined_df)



    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
