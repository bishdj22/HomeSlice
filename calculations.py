import pandas as pd
import requests
import zillow
# import pprint as pp
import json
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect


connection_string = "postgres:apartment@homeslice.cjnrjw08kldx.us-east-2.rds.amazonaws.com:5432/HomeSliceDB"
engine = create_engine(f'postgresql://{connection_string}')
api = zillow.ValuationApi()
key = "X1-ZWz17fdl35adqj_3bebs"

def address_search(address, postal_code):
    connection_string = "postgres:apartment@homeslice.cjnrjw08kldx.us-east-2.rds.amazonaws.com:5432/HomeSliceDB"
    engine = create_engine(f'postgresql://{connection_string}')
    api = zillow.ValuationApi()
    key = "X1-ZWz17fdl35adqj_3bebs"

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

    zip_for_model = combined_df['zipcode']
    
    # Call ML model
        # if x == true then 15-30% else 0-15%

    #
    
    return(combined_df)