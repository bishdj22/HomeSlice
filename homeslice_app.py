from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_marsDB

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    """Return Homepage"""

    # Return template and data
    return render_template("index.html")


# Route that will trigger the scrape function
@app.route("/scrape")
def home_search():


    # mars = mongo.db.mars
    # Run the scrape function
    home_value = HomeSlice_master.scrape_test()

    # Update the Mongo database using update and upsert=True
    # mars.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
