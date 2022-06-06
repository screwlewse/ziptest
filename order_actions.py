
from products import Products
from inventory import Inventory
from order import Order

class OrderInterface:

    def __init__(self):
        # required instances
        self.products = Products()
        self.inventory = Inventory()
        self.order = Order()
        # "persistent" storage
        self.products_data = {}
        self.inventory_data = {}
        self.order_data = []
        self.shipment_data = []
        self.backorders = []

    def init_catalog(self, product_info: str) -> str:
        self.products_data = self.products.create(product_info)
        return self.products_data

    def process_restock(self, new_inventory):
        self.inventory_data.update(self.inventory.add(new_inventory, self.products_data))
        return new_inventory

    def process_order(self, new_order):
        current_order, current_shipments, backorders = self.order.ship(new_order, self.products_data, self.inventory_data)
        self.order_data.append(current_order)
        self.shipment_data.append(current_shipments)
        self.backorders.append(backorders)
        return self.order_data, self.shipment_data, backorders
