class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name  # название
        self.description = description  # описание
        self.__price = price  # цена
        self.quantity = quantity  # количество в наличии

    @classmethod
    def new_product(cls, product_data: dict):
        """ "Метод для создания нового продукта"""
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

    def __str__(self):
        """Метод для отображения информации для разработчика"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод возвращает сумму произведений цены на количество или сумму всех товаров на складе."""
        if type(self) == type(other):
            total_amount = self.quantity * self.price + other.quantity * other.price
            return total_amount
        raise TypeError


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency  # производительность
        self.model = model  # модель
        self.memory = memory  # объем встроенной памяти
        self.color = color  # цвет


class LawnGrass(Product):

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country  # страна-производитель
        self.germination_period = germination_period  # срок прорастания
        self.color = color  # цвет


class Category:
    name: str
    description: str
    products: list
    product_count: int = 0
    category_count: int = 0

    def __init__(self, name, description, products):
        self.name = name  # название
        self.description = description  # описание
        self.__products = products if products else []  # список товаров категории
        self.product_count = len(self.__products) if products else 0  # количество товаров.
        Category.category_count += 1  # количество категорий
        Category.product_count += len(self.__products) if products else 0

    def add_product(self, new_product: Product):
        """Метод для добавления нового продукта в категорию, при совпадении наименования -
        установление максимального прайса и сложение количества"""
        if not isinstance(new_product, Product):
            raise TypeError
        for product in self.__products:
            if product.name == new_product.name:
                product.price = max(product.price, new_product.price)
                product.quantity += new_product.quantity
                break

        self.__products.append(new_product)
        self.product_count += 1
        Category.product_count += 1

    def __str__(self):
        """Метод __str__ рассчитывает общее количество товаров на складе (quantity) для каждого продукта
        в приватном атрибуте products"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self):
        lines = []
        for product in self.__products:
            lines.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(lines)
