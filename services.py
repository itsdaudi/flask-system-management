import requests

BASE_URL = "https://world.openfoodfacts.org/api/v0/product"
SEARCH_URL = "https://world.openfoodfacts.org/cgi/search.pl"
#fetch product by barcode from Open Food Facts API
def fetch_product_by_barcode(barcode):

    try:
        url = f"{BASE_URL}/{barcode}.json"

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data.get("status") == 1:
            return data.get("product")

        return None

    except requests.exceptions.RequestException as error:
        print(f"API Error: {error}")
        return None

