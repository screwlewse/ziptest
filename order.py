from itertools import product
from turtle import back
from settings import PACKAGE_LIMIT_GRAMS

class Order:

    def __init__(self):
        self.backorders = []
        self.order_shipments = []

    def ship(self, order: dict, product_data: list, inventory_data: list):
        shipment = []
        shipment_weight = 0
        for item in order["requested"]:
            id = item["product_id"]
            quantity = item["quantity"]
            # do the products exist in products and is there enough
            if not product_data.get(id):
                raise ValueError(f"No product found for product_id: {id}.")
            # is there enough inventory to fill the order?
            if inventory_data[id]["quantity"] < quantity:
                backordered_quantity = self.add_to_backorder(quantity, inventory_data[id]["quantity"])
                item["quantity"] = quantity - backordered_quantity
            # is the order larger than one shipment?
            item_weight = product_data[id]["mass_g"]
            if item_weight + shipment_weight < PACKAGE_LIMIT_GRAMS:
                shipment.append(item)
                shipment_weight += item_weight
            else:
                self.append_and_ship_order(order["order_id"], shipment)
                # reset counters
                shipment_weight = 0
                shipment = []
        # ship the items still pending
        if len(shipment) > 0:
            self.append_and_ship_order(order["order_id"], shipment)
        return order, self.order_shipments, self.backorders

    def append_and_ship_order(self, order_id: int, shipment: list) -> None:
        shipped_order = self.ship_items(order_id, shipment)
        self.order_shipments.append(shipped_order)

    def add_to_backorder(self, order_quantity, inventory_quantity):
        backordered_quantity = order_quantity - inventory_quantity
        missing_products = {
            "product_id": id,
            "quantity": backordered_quantity
        }
        self.backorders.append(missing_products)
        return backordered_quantity

    def ship_items(self, order_id: int, shipment: list) -> dict:
        shipment_payload = {
            "order_id": order_id,
            "shipped": shipment
        }
        print(f"shipping: {shipment_payload}") # stubbed api call or kafka topic
        return shipment_payload




