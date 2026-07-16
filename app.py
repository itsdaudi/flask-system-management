from flask import Flask, jsonify, request
from flask_cors import CORS
from inventory import Inventory
from services import fetch_product_by_barcode

app = Flask(__name__)
CORS(app)

#Home route
@app.route("/")
def home():
    return jsonify({
        "message": "Inventory Management REST API",
        "available_routes": {
            "GET /Inventory": "View all inventory",
            "GET /Inventory/<id>": "View one product",
            "POST /Inventory": "Add product",
            "PATCH /Inventory/<id>": "Update product",
            "DELETE /Inventory/<id>": "Delete product",
            "GET /lookup/<barcode>": "Lookup OpenFoodFacts product"
        }
    })
#get all products in inventory
@app.route("/Inventory", methods=["GET"])
def get_Inventory():
    return jsonify(Inventory), 200

#get one product in inventory
@app.route("/Inventory/<int:item_id>", methods=["GET"])
def get_product(item_id):

    for item in Inventory:
        if item["id"] == item_id:
            return jsonify(item), 200

    return jsonify({
        "error": "Product not found"
    }), 404

#add product to inventory
@app.route("/Inventory", methods=["POST"])
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
        [item["id"] for item in Inventory],
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

    Inventory.append(new_product)

    return jsonify({
        "message": "Product added successfully.",
        "product": new_product
    }), 201

#update product in inventory
@app.route("/Inventory/<int:item_id>", methods=["PATCH"])
def update_product(item_id):

    data = request.get_json()

    for item in Inventory:

        if item["id"] == item_id:

            if "barcode" in data:
                item["barcode"] = data["barcode"]

            if "product_name" in data:
                item["product_name"] = data["product_name"]

            if "brand" in data:
                item["brand"] = data["brand"]

            if "category" in data:
                item["category"] = data["category"]

            if "ingredients" in data:
                item["ingredients"] = data["ingredients"]

            if "quantity" in data:
                item["quantity"] = data["quantity"]

            if "price" in data:
                item["price"] = data["price"]

            return jsonify({
                "message": "Product updated successfully.",
                "product": item
            }), 200

    return jsonify({
        "error": "Product not found."
    }), 404

#delete product in inventory
@app.route("/Inventory/<int:item_id>", methods=["DELETE"])
def delete_product(item_id):

    for item in Inventory:

        if item["id"] == item_id:

            Inventory.remove(item)

            return jsonify({
                "message": "Product deleted successfully."
            }), 200

    return jsonify({
        "error": "Product not found."
    }), 404

#lookup product by barcode
@app.route("/lookup/<barcode>", methods=["GET"])
def lookup_product(barcode):

    product = fetch_product_by_barcode(barcode)

    if product is None:

        return jsonify({
            "error": "Product not found."
        }), 404

    return jsonify({
        "product_name": product.get("product_name"),
        "brand": product.get("brands"),
        "ingredients": product.get("ingredients_text"),
        "category": product.get("categories"),
        "image": product.get("image_url")
    }), 200
#Run the app
if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )






