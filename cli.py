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

#add product function to prompt user for product details and send a POST request to the API
def add_product():

    print_separator()

    try:

        barcode = input("Barcode: ").strip()
        product_name = input("Product Name: ").strip()
        brand = input("Brand: ").strip()
        category = input("Category: ").strip()

        quantity = int(input("Quantity: "))
        price = float(input("Price: "))

        payload = {
            "barcode": barcode,
            "product_name": product_name,
            "brand": brand,
            "category": category,
            "quantity": quantity,
            "price": price
        }

        response = requests.post(
            f"{BASE_URL}/inventory",
            json=payload,
            timeout=5
        )

        if response.status_code == 201:
            print("\nProduct added successfully.")

        else:
            print(response.json())

    except ValueError:
        print("Quantity must be an integer and price must be numeric.")

    except requests.exceptions.RequestException:
        handle_connection_error()

#update product function to prompt user for product ID and new details, then send a PATCH request to the API
def update_product():

    print_separator()

    try:

        product_id = int(input("Product ID: "))
        quantity = int(input("New Quantity: "))
        price = float(input("New Price: "))

        payload = {
            "quantity": quantity,
            "price": price
        }

        response = requests.patch(
            f"{BASE_URL}/inventory/{product_id}",
            json=payload,
            timeout=5
        )

        if response.status_code == 200:
            print("Product updated successfully.")

        elif response.status_code == 404:
            print("Product not found.")

        else:
            print(response.json())

    except ValueError:
        print("Invalid numeric input.")

    except requests.exceptions.RequestException:
        handle_connection_error()

#delete product function to prompt user for product ID and send a DELETE request to the API
def delete_product():

    print_separator()

    try:

        product_id = int(input("Product ID: "))

        response = requests.delete(
            f"{BASE_URL}/inventory/{product_id}",
            timeout=5
        )

        if response.status_code == 200:
            print("Product deleted successfully.")

        elif response.status_code == 404:
            print("Product not found.")

        else:
            print(response.json())

    except ValueError:
        print("Invalid ID.")

    except requests.exceptions.RequestException:
        handle_connection_error()

#search product function to prompt user for barcode and send a GET request to the API
def search_product():

    print_separator()

    barcode = input("Enter barcode: ").strip()

    try:

        response = requests.get(
            f"{BASE_URL}/lookup/{barcode}",
            timeout=10
        )

        if response.status_code == 200:

            product = response.json()

            print("\nProduct Found")
            print("-" * 40)
            print("Name:", product.get("product_name", "N/A"))
            print("Brand:", product.get("brand", "N/A"))
            print("Category:", product.get("category", "N/A"))
            print("Ingredients:", product.get("ingredients", "N/A"))
            print("Image:", product.get("image", "N/A"))

        elif response.status_code == 404:
            print("Product not found.")

        else:
            print(response.json())

    except requests.exceptions.RequestException:
        handle_connection_error()

#menu function to display the main menu and handle user input
def menu():

    while True:

        print_separator()

        print("Inventory Management System")
        print("1. View Inventory")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Find Product (OpenFoodFacts)")
        print("6. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            view_inventory()

        elif choice == "2":
            add_product()

        elif choice == "3":
            update_product()

        elif choice == "4":
            delete_product()

        elif choice == "5":
            search_product()

        elif choice == "6":
            print("\nGoodbye!")
            break

        else:
            print("Invalid option. Please choose 1-6.")

#start the CLI application
if __name__ == "__main__":
    menu()            









