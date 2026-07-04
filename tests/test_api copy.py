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
