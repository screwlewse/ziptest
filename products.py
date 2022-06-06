
class Products:

    def __init__(self):
        self.products = {}

    def create(self, product_info: list) -> list:
        print("Adding new products")
        if len(self.products) > 0:
            raise ValueError("No products specified")
        for product in product_info:
            if product["product_id"] in self.products:
                raise ValueError("Duplicate product found in list")
            self.products[product["product_id"]] = product
        print("Products created")
        return self.products

    def get(self, product_id: int = None) -> list:
        if not product_id:
            return self.products
        try:
            return [self.products[product_id]]
        except KeyError as exc:
            raise exc

