from unicodedata import category

from src.classes import Category
from tests.conftest import category_1


def test_product_init(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_category_init(category_1):
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert Category.product_count == 3
    assert Category.category_count == 1