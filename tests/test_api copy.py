#unit test for flask rest api
from inventory import inventory

#home route test
def test_home(client):
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert "message" in data