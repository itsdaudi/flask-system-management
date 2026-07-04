"""
test_services.py

Unit tests for services.py (OpenFoodFacts API integration)
"""

from unittest.mock import patch
import requests

from services import (
    fetch_product_by_barcode,
    fetch_product_by_name,
    enrich_inventory_item
)


# ---------------------------------------
# Test fetch_product_by_barcode() SUCCESS
# ---------------------------------------
@patch("services.requests.get")
def test_fetch_product_by_barcode_success(mock_get):

    mock_get.return_value.status_code = 200
    mock_get.return_value.raise_for_status.return_value = None

    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Organic Almond Milk",
            "brands": "Silk",
            "ingredients_text": "Filtered water, almonds",
            "categories": "Plant-Based Drinks",
            "image_url": "https://example.com/image.jpg"
        }
    }

    product = fetch_product_by_barcode("737628064502")

    assert product is not None
    assert product["product_name"] == "Organic Almond Milk"
    assert product["brands"] == "Silk"


# ---------------------------------------
# Test barcode NOT FOUND
# ---------------------------------------
@patch("services.requests.get")
def test_fetch_product_by_barcode_not_found(mock_get):

    mock_get.return_value.status_code = 200
    mock_get.return_value.raise_for_status.return_value = None

    mock_get.return_value.json.return_value = {
        "status": 0
    }

    product = fetch_product_by_barcode("000000")

    assert product is None


# ---------------------------------------
# Test API Connection Error
# ---------------------------------------
@patch("services.requests.get")
def test_fetch_product_connection_error(mock_get):

    mock_get.side_effect = requests.exceptions.ConnectionError

    product = fetch_product_by_barcode("737628064502")

    assert product is None


# ---------------------------------------
# Test Search by Product Name
# ---------------------------------------
@patch("services.requests.get")
def test_fetch_product_by_name(mock_get):

    mock_get.return_value.status_code = 200
    mock_get.return_value.raise_for_status.return_value = None

    mock_get.return_value.json.return_value = {
        "products": [
            {
                "product_name": "Nutella",
                "brands": "Ferrero",
                "ingredients_text": "Sugar, palm oil",
                "categories": "Spreads"
            }
        ]
    }

    product = fetch_product_by_name("Nutella")

    assert product is not None
    assert product["product_name"] == "Nutella"


# ---------------------------------------
# Test Product Name Not Found
# ---------------------------------------
@patch("services.requests.get")
def test_fetch_product_by_name_not_found(mock_get):

    mock_get.return_value.status_code = 200
    mock_get.return_value.raise_for_status.return_value = None

    mock_get.return_value.json.return_value = {
        "products": []
    }

    product = fetch_product_by_name("Unknown Product")

    assert product is None


# ---------------------------------------
# Test enrich_inventory_item()
# ---------------------------------------
@patch("services.fetch_product_by_barcode")
def test_enrich_inventory_item(mock_lookup):

    mock_lookup.return_value = {
        "product_name": "Organic Almond Milk",
        "brands": "Silk",
        "ingredients_text": "Filtered water, almonds",
        "categories": "Plant-Based Drinks",
        "image_url": "https://example.com/image.jpg"
    }

    item = {
        "id": 1,
        "barcode": "737628064502",
        "quantity": 20,
        "price": 350
    }

    updated_item = enrich_inventory_item(item)

    assert updated_item["product_name"] == "Organic Almond Milk"
    assert updated_item["brand"] == "Silk"
    assert updated_item["category"] == "Plant-Based Drinks"
    assert updated_item["ingredients"] == "Filtered water, almonds"
    assert updated_item["image"] == "https://example.com/image.jpg"


# ---------------------------------------
# Test enrich_inventory_item()
# Without Barcode
# ---------------------------------------
def test_enrich_inventory_without_barcode():

    item = {
        "id": 1,
        "quantity": 10,
        "price": 100
    }

    updated = enrich_inventory_item(item)

    assert updated == item


# ---------------------------------------
# Test enrich_inventory_item()
# Product Not Found
# ---------------------------------------
@patch("services.fetch_product_by_barcode")
def test_enrich_inventory_not_found(mock_lookup):

    mock_lookup.return_value = None

    item = {
        "id": 1,
        "barcode": "999999",
        "quantity": 10,
        "price": 120
    }

    updated = enrich_inventory_item(item)

    assert updated == item