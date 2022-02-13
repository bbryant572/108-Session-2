from flask import Flask
from mock_data import catalog
import json
from about_me import me

# create the server/app
app = Flask("server")


@app.route("/myaddress")
def home_address():
    address = me["address"]
    # return address["street" + " " + address["city"]]
    return f"{address['street']} {address['city']}"


@app.route("/", methods=["get"])
def home_page():
    return "Under Construction!"


@app.route("/about")
def about_me():
    return "Brett Bryant"


@app.route("/test")
def test():
    return "I'm a simple test"


##################################################
############### API ENDPOINT #####################
##################################################


@app.route("/api/catalog")
def get_catalog():
    return json.dumps(catalog)


# start the server
app.run(debug=True)
