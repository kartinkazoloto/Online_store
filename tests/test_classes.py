from src.classes import Category, Product
from tests.conftest import category_1


def test_product_init(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_category_init(category_1):
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert Category.product_count == 3
    assert Category.category_count == 1


def test_product_new_product():
    """Проверка класс-метода new_product."""
    data = {"name": "Ноутбук", "description": "Игровой", "price": 70000.0, "quantity": 3}
    product = Product.new_product(data)
    assert isinstance(product, Product)
    assert product.name == "Ноутбук"
    assert product.description == "Игровой"
    assert product.price == 70000.0
    assert product.quantity == 3


def test_product_price_getter():
    """Проверка геттера price."""
    product = Product("Мышь", "Беспроводная", 1500.0, 20)
    assert product.price == 1500.0


def test_product_price_setter_zero_or_negative(capsys):
    """Сеттер: цена ≤ 0 — должно вывести сообщение, цена не меняется."""
    product = Product("Наушники", "Bluetooth", 2500.0, 8)

    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out

    assert product.price == 2500.0

    product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out

    assert product.price == 2500.0


def test_add_product_new():
    """Добавление нового продукта в категорию."""
    category = Category("Бытовая техника", "Для дома", [])
    product = Product("Пылесос", "Робот", 25000.0, 5)
    category.add_product(product)
    assert "Пылесос, 25000.0 руб. Остаток: 5 шт." in category.products
    assert category.product_count == 1


def test_add_product_duplicate_update():
    """Добавление продукта с тем же именем — должно обновить цену и количество."""
    existing = Product("Кофемашина", "Автоматическая", 30000.0, 3)
    category = Category("Кухня", "Техника для приготовления", [existing])

    new = Product("Кофемашина", "Обновлённая", 32000.0, 2)  # цена выше, кол-во +2
    category.add_product(new)
    expected_line = "Кофемашина, 32000.0 руб. Остаток: 5 шт."
    assert expected_line in category.products
    assert category.product_count == 1
