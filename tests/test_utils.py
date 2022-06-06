

def mock_product(mass_g = 700, product_name = "Test Product A", product_id = 0):
    return [_build_product_dict(mass_g, product_name, product_id)]

def mock_inventory(product_id: int = 0, quantity: int = 1):
    return [
        {
            "product_id": product_id,
            "quantity": quantity
        }
    ]

def mock_product_dict_data(mass_g = 700, product_name = "Test Product A", product_id = 0):
    return {
        product_id: _build_product_dict(mass_g, product_name, product_id)
    }

def _build_product_dict(mass_g, product_name, product_id):
    return {
        "mass_g": mass_g,
        "product_name":  product_name,
        "product_id": product_id
    }