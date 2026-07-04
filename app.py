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

#get one product in inventory
@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_product(item_id):

    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item), 200

    return jsonify({
        "error": "Product not found"
    }), 404

#add product to inventory
@app.route("/inventory", methods=["POST"])
def add_product():

    data = request.get_json()

    required_fields = [
        "barcode",
        "product_name",
        "quantity",
        "price"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"{field} is required."
            }), 400

    new_id = max(
        [item["id"] for item in inventory],
        default=0
    ) + 1

    new_product = {
        "id": new_id,
        "barcode": data["barcode"],
        "product_name": data["product_name"],
        "brand": data.get("brand", ""),
        "category": data.get("category", ""),
        "ingredients": data.get("ingredients", ""),
        "quantity": data["quantity"],
        "price": data["price"]
    }

    inventory.append(new_product)

    return jsonify({
        "message": "Product added successfully.",
        "product": new_product
    }), 201





