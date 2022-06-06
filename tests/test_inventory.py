import pytest

from inventory import Inventory
from tests.test_utils import (
    mock_inventory,
    mock_product,
    mock_product_dict_data
)

def test_add_inventory():
    products_data_dict = mock_product_dict_data()
    inventory_data = mock_inventory()
    inventory = Inventory()
    response = inventory.add(inventory_data, products_data_dict)
    assert response[0]["product_id"] == 0
    assert response[0]["quantity"] == 1

def test_add_nonexistent_inventory():
    products_data_dict = mock_product_dict_data()
    inventory_data = mock_inventory(product_id = 2)
    inventory = Inventory()
    with pytest.raises(Exception) as e:
        inventory.add(inventory_data, products_data_dict)
    assert e.type == ValueError
