#cli inventory management system run with rest api
import requests

BASE_URL = "http://127.0.0.1:5555"
#help function to print a separator line
def print_separator():
    print("\n" + "=" * 60)


def handle_connection_error():
    print("\nError: Could not connect to the Flask API.")
    print("Make sure app.py is running on http://127.0.0.1:5555\n")

#view inventory function to fetch and display all products in the inventory
def view_inventory():
    try:
        response = requests.get(f"{BASE_URL}/inventory", timeout=5)

        if response.status_code == 200:

            products = response.json()

            if not products:
                print("\nInventory is empty.")
                return

            print_separator()

            for product in products:
                print(f"ID: {product['id']}")
                print(f"Name: {product['product_name']}")
                print(f"Barcode: {product['barcode']}")
                print(f"Brand: {product.get('brand', 'N/A')}")
                print(f"Quantity: {product['quantity']}")
                print(f"Price: KES {product['price']}")
                print("-" * 60)

        else:
            print("Unable to fetch inventory.")

    except requests.exceptions.RequestException:
        handle_connection_error()


