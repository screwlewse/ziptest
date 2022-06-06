import pytest
from products import Products
from tests.test_utils import mock_product

def test_create_initial_products():
    product = Products()
    response = product.create(mock_product())
    assert response[0]["mass_g"] == 700

def test_create_duplicate_products():
    product = Products()
    mock_products = mock_product()
    mock_products.append(mock_product()[0])
    with pytest.raises(Exception) as e:
        product.create(mock_products)
    assert e.type == ValueError

def test_products_already_initialized():
    product = Products()
    product.create(mock_product())
    with pytest.raises(Exception) as e:
        response = product.create(mock_product())
    assert e.type == ValueError

def test_get_one_product():
    product = Products()
    mock_products = mock_product()
    mock_products.append(mock_product(product_id=1)[0])
    product.create(mock_products)
    response = product.get(1)
    assert response[0]["product_id"] == 1

def test_get_many_products():
    product = Products()
    mock_products = mock_product()
    mock_products.append(mock_product(product_id=1)[0])
    product.create(mock_products)
    response = product.get()
    assert type(response) == dict
    assert response[0]["product_id"] == 0
    assert response[1]["product_id"] == 1



