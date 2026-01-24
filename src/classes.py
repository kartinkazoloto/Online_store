class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, product_data: dict):
        name = product_data['name']
        description = product_data['description']
        price = product_data['price']
        quantity = product_data['quantity']
        return cls(name, description, price, quantity)


class Category:
    name: str
    description: str
    products: list
    product_count: int = 0
    category_count: int = 0

    def __init__(self, name, description, products):
        # self.products = []
        self.name = name
        self.description = description
        self.__products = products if products else []
        self.product_count = len(self.__products) if products else 0
        Category.category_count += 1
        Category.product_count += len(self.__products) if products else 0


    def add_product(self, product: Product):
        self.__products.append(product)
        self.product_count += 1


    @property
    def products(self):
        lines = []
        for product in self.__products:
            lines.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(lines)
