import pytest
from order_actions import OrderInterface


def test_create_():
    order_actions = OrderInterface()
    response = order_actions.init_catalog(order_actions.product_info_data)
    assert type(response) == dict
