"""
test_cli.py

Unit tests for the CLI application.
"""

from unittest.mock import patch
import cli


# -------------------------
# VIEW INVENTORY
# -------------------------
@patch("cli.requests.get")
@patch("builtins.print")
def test_view_inventory(mock_print, mock_get):

    mock_get.return_value.status_code = 200

    mock_get.return_value.json.return_value = [
        {
            "id": 1,
            "product_name": "Milk",
            "barcode": "12345",
            "brand": "Brookside",
            "quantity": 10,
            "price": 120
        }
    ]

    cli.view_inventory()

    assert mock_get.called
    assert mock_print.called


# -------------------------
# ADD PRODUCT
# -------------------------
@patch("cli.requests.post")
@patch("builtins.input", side_effect=[
    "123456789",
    "Milk",
    "Brookside",
    "Dairy",
    "20",
    "150"
])
@patch("builtins.print")
def test_add_product(mock_print, mock_input, mock_post):

    mock_post.return_value.status_code = 201

    cli.add_product()

    assert mock_post.called
    assert mock_print.called


# -------------------------
# UPDATE PRODUCT
# -------------------------
@patch("cli.requests.patch")
@patch("builtins.input", side_effect=[
    "1",
    "50",
    "250"
])
@patch("builtins.print")
def test_update_product(mock_print, mock_input, mock_patch):

    mock_patch.return_value.status_code = 200

    cli.update_product()

    assert mock_patch.called
    assert mock_print.called


# -------------------------
# DELETE PRODUCT
# -------------------------
@patch("cli.requests.delete")
@patch("builtins.input", side_effect=[
    "1"
])
@patch("builtins.print")
def test_delete_product(mock_print, mock_input, mock_delete):

    mock_delete.return_value.status_code = 200

    cli.delete_product()

    assert mock_delete.called
    assert mock_print.called


# -------------------------
# SEARCH PRODUCT
# -------------------------
@patch("cli.requests.get")
@patch("builtins.input", side_effect=[
    "737628064502"
])
@patch("builtins.print")
def test_search_product(mock_print, mock_input, mock_get):

    mock_get.return_value.status_code = 200

    mock_get.return_value.json.return_value = {
        "product_name": "Organic Almond Milk",
        "brand": "Silk",
        "category": "Plant-Based Drinks",
        "ingredients": "Filtered water, almonds"
    }

    cli.search_product()

    assert mock_get.called
    assert mock_print.called


# -------------------------
# CONNECTION ERROR
# -------------------------
@patch(
    "cli.requests.get",
    side_effect=Exception("Connection failed")
)
@patch("builtins.print")
def test_connection_error(mock_print, mock_get):

    try:
        cli.view_inventory()
    except Exception:
        pass

    assert mock_get.called