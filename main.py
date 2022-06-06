# This file is to automate the interactions, not code pre se

import json
from pprint import pprint

from order_actions import OrderInterface

# Initialize the actions
zip = OrderInterface()

# Initialize the catalog with empty products
with open("data/product_info.json") as f:
    zip.init_catalog(json.loads(f.read()))
    pprint(zip.products_data)

# Add products to inventory
with open("data/restock.json") as f:
    zip.process_restock(json.loads(f.read()))
    pprint(zip.inventory_data)

# Create the orders
with open("data/orders.json") as f:
    zip.process_order(json.loads(f.read()))
    pprint(zip.order_data)
    pprint(zip.shipment_data)
    pprint(zip.backorders)