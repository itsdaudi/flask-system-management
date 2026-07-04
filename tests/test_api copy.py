#unit test for flask rest api
from inventory import inventory

#home route test
def test_home(client):
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert "message" in data

#get all products route test
def test_get_inventory(client):

    response = client.get("/inventory")

    assert response.status_code == 200

    data = response.get_json()

    assert isinstance(data, list)

#get single product route test
def test_get_single_product(client):

    response = client.get("/inventory/1")

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == 1

#test invalid product route test
def test_get_invalid_product(client):

    response = client.get("/inventory/999")

    assert response.status_code == 404


# -------------------------
# ADD PRODUCT
# -------------------------
def test_add_product(client):

    payload = {
        "barcode": "999999999999",
        "product_name": "Test Product",
        "brand": "Testing",
        "category": "Testing",
        "ingredients": "Testing",
        "quantity": 15,
        "price": 100
    }

    response = client.post(
        "/inventory",
        json=payload
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["message"] == "Product added successfully."

    assert data["product"]["product_name"] == "Test Product"


# -------------------------
# ADD PRODUCT
# MISSING FIELD
# -------------------------
def test_add_product_missing_field(client):

    payload = {
        "product_name": "Milk"
    }

    response = client.post(
        "/inventory",
        json=payload
    )

    assert response.status_code == 400


# -------------------------
# UPDATE PRODUCT
# -------------------------
def test_update_product(client):

    payload = {
        "price": 500,
        "quantity": 100
    }

    response = client.patch(
        "/inventory/1",
        json=payload
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["product"]["price"] == 500
    assert data["product"]["quantity"] == 100


# -------------------------
# UPDATE INVALID PRODUCT
# -------------------------
def test_update_invalid_product(client):

    payload = {
        "price": 100
    }

    response = client.patch(
        "/inventory/999",
        json=payload
    )

    assert response.status_code == 404


# -------------------------
# DELETE PRODUCT
# -------------------------
def test_delete_product(client):

    client.post(
        "/inventory",
        json={
            "barcode": "555555",
            "product_name": "Delete Me",
            "quantity": 5,
            "price": 50
        }
    )

    product_id = inventory[-1]["id"]

    response = client.delete(
        f"/inventory/{product_id}"
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["message"] == "Product deleted successfully."


# -------------------------
# DELETE INVALID PRODUCT
# -------------------------
def test_delete_invalid_product(client):

    response = client.delete(
        "/inventory/999"
    )

    assert response.status_code == 404