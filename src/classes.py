class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер для получения текущей цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер приватного атрибута __price, позволяет изменить цену продукта,
        только, если значение новой цены больше нуля"""

        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif self.__price <= new_price:
            self.__price = new_price
        else:
            print(
                """Новая цена продукта меньше текущей. Если вы согласны с понижением цены,
                введите английскую "y", иначе, введите любой другой символ или нажмите Enter."""
            )
            user_accept = input().lower()
            if user_accept == "y":
                self.__price = new_price
            print(f"Установлена цена продукта: {self.__price} руб.")


class Category:
    name: str
    description: str
    products: list
    product_count: int = 0
    category_count: int = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []
        self.product_count = len(self.__products) if products else 0
        Category.category_count += 1
        Category.product_count += len(self.__products) if products else 0

    def add_product(self, new_product: Product):
        for product in self.__products:
            if new_product.name == product.name:
                new_product.price = max(new_product.price, product.price)
                new_product.quantity += product.quantity
                return

        self.__products.append(new_product)
        self.product_count += 1
        Category.product_count += 1

    @property
    def products(self):
        lines = []
        for product in self.__products:
            lines.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(lines)
