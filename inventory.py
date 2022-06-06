
class Inventory:

    def __init__(self):
        self.inventory = {}

    def add(self, inventory: list, products: list) -> list:
        print("Stocking items into the inventory")
        # NOTE: Passing around data (in this case, products) as args isnt recommended
        # Of course, this would not be an issue with actual persistent storage
        for item in inventory:
            if item["product_id"] not in products:
                raise ValueError(f"product_id: {item['product_id']} not found")
            self.inventory[item["product_id"]] = item
        print("Inventory items stocked")
        return self.inventory

    # def get(self):
    #     return

    # def remove(self):
    #     return
