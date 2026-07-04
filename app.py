from flask import Flask, jsonify, request
from inventory import inventory
from services import fetch_product_by_barcode

app = Flask(__name__)

#Home route
@app.route("/")
def home():
    return jsonify({
        "message": "Inventory Management REST API",
        "available_routes": {
            "GET /inventory": "View all inventory",
            "GET /inventory/<id>": "View one product",
            "POST /inventory": "Add product",
            "PATCH /inventory/<id>": "Update product",
            "DELETE /inventory/<id>": "Delete product",
            "GET /lookup/<barcode>": "Lookup OpenFoodFacts product"
        }
    })
#get all products in inventory
@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200

