import pandas as pd
import requests
import zillow
import sys
import json
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect
from config import zillow_key, database_key

#Database and API connections

# connection_string = "postgres:apartment@homeslice.cjnrjw08kldx.us-east-2.rds.amazonaws.com:5432/HomeSliceDB"
connection_string = database_key
engine = create_engine(f'postgresql://{connection_string}')
api = zillow.ValuationApi()
key = zillow_key

#Function to call Zillow API and return address and Zestimate, convert results to dataframe and append to database

def address_search(address, postal_code):
    connection_string = database_key
    engine = create_engine(f'postgresql://{connection_string}')
    api = zillow.ValuationApi()
    key = zillow_key

    #API call and results returned
    try:
        request_data = api.GetSearchResults(key, address, postal_code)
        result = request_data.get_dict()
        address = result['full_address']
        zestimate = result['zestimate']

        #Combined returned results to a single dictionary and then to a dataframe
        comb_dict = dict(zestimate)
        comb_dict.update(address)
        combined_df = pd.DataFrame.from_dict(comb_dict, orient='index').T

        #Add Risk Adjustment calculations columns to the data frame
        combined_df['risk_adj_value'] = (combined_df['amount']*.85) #Risk adjusting home by 15%, reducing home val by 15%
        combined_df['max_cash_limit'] = combined_df['risk_adj_value']*.30 #Not to buy more than 30% of someones home equity, to avoid controlling interest
        
        #Log the data frame to the database using SQL
        combined_df.to_sql(name='zillow', con=engine, if_exists='append', index=False)
        print("connecting to db")



        #Using API-returned Zip Code, compare that value with our risk data table ('sales_price' table). Will return True/False response from the 'equity_risk' column
        def result_getter(postal_code):
            connection = engine.connect()
            query = "select sp.equity_risk from sales_price sp where sp.zip_code = " + postal_code + ";"
            result = connection.execute(query)
            for i in result:
                results = i
            return results
        results = result_getter(postal_code)
        print("query finished")
        print(results[0])
        print("Success")
        
        
        # Decision tree - if True, allowable investment 30% of risk adj home value. If False, 10% of risk adj home value
        if results[0] == True:
            offer = combined_df['max_cash_limit']
            
        else:
            offer = combined_df['risk_adj_value']*.10
        
        
        return (combined_df['amount'], offer)

    except:
        return("Bad Address")