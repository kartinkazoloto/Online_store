import pytest

from src.classes import Category, Product
from tests.conftest import category_1, product_5


def test_product_init(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_product_init_0():
    with pytest.raises(ValueError) as e:
        Product(
            name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=0
        )
    assert "Товар с нулевым количеством не может быть добавлен" in str(e.value)


def test_product_smatrphone_init(product_4):
    assert product_4.name == "Samsung Galaxy S23 Ultra"
    assert product_4.description == "256GB, Серый цвет, 200MP камера"
    assert product_4.price == 180000.0
    assert product_4.quantity == 5
    assert product_4.efficiency == 95.5
    assert product_4.model == "S23 Ultra"
    assert product_4.memory == 256
    assert product_4.color == "Серый"


def test_product_lawngrass_init(product_5):
    assert product_5.name == "Газонная трава"
    assert product_5.description == "Элитная трава для газона"
    assert product_5.price == 500.0
    assert product_5.quantity == 5
    assert product_5.country == "Россия"
    assert product_5.germination_period == "7 дней"
    assert product_5.color == "Зеленый"


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
    assert category.product_count == 2


def test_product__str__():
    product = Product("Пылесос", "Робот", 25000.0, 5)
    result = str(product)
    assert result == "Пылесос, 25000.0 руб. Остаток: 5 шт."


def test_product__add__(product_5):
    prod_1 = Product("Кофемашина", "Автоматическая", 30000.0, 3)
    prod_2 = Product("Пылесос", "Робот", 25000.0, 5)
    result = prod_1 + prod_2
    assert result == 215000.0
    with pytest.raises(TypeError):
        Product.__add__(prod_1, product_5)


def test_add_product_wrong_type():
    """Тест: добавление объекта не типа Product вызывает TypeError."""
    category = Category("Электроника", "Гаджеты", [])

    with pytest.raises(TypeError):
        category.add_product("не продукт")

    with pytest.raises(TypeError):
        category.add_product(123)

    with pytest.raises(TypeError):
        category.add_product({"name": "fake"})


def test_category__str__():
    """Метод __str__ рассчитывает общее количество товаров на складе (quantity)
    для каждого продукта в приватном атрибуте products"""
    existing = Product("Кофемашина", "Автоматическая", 30000.0, 3)
    category = Category("Кухня", "Техника для приготовления", [existing])
    result = str(category)
    assert result == "Кухня, количество продуктов: 3 шт."


def test_middle_price():
    cat_0 = Category("Пустая категория", "Категория без продуктов", [])
    result = cat_0.middle_price()
    assert result == 0
