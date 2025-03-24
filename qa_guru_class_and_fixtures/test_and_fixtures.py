"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from qa_guru_class_and_fixtures.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 500)


@pytest.fixture
def cart(product):
    return Cart()


@pytest.fixture
def product1():
    return Product("notebook", 213, "This is a notebook", 500)

@pytest.fixture
def product2():
    return Product("phone", 200, "This is a iphone 13 pro", 500)



class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(500) is True
        assert product.check_quantity(499) is True
        assert product.check_quantity(501) is False


    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(100)
        assert product.quantity == 400


    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(product.quantity + 1)

class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self , cart , product1 ,product2, product):
        cart.add_product(product1, buy_count=2)
        assert cart.products[product1] == 20

        cart.add_product(product2, buy_count=3)
        assert cart.products[product2] == 30

        cart.add_product(product2 , buy_count=10)
        assert cart.products[product2] == 13

        cart.add_product(product1, buy_count=70)
        assert cart.products[product1] == 100

        # Проверка добавления максимального допустимого количества продукта
        max_allowed = 150
        cart.add_product(product2, buy_count=max_allowed)
        assert cart.products[product2] == 210

    def test_remove_product(self, cart , product1):
        cart.add_product(product1, buy_count=5)

        cart.remove_product(product1, remove_count=2)
        assert cart.products[product1] == 3

        cart.clear_cart()
        assert len(cart.products) == 0

    def test_full_clear_product(self , cart , product1 ):
        cart.add_product(product1 , 3)
        cart.remove_product(product1, remove_count=3)
        assert product1 not in cart.products

        cart.add_product(product1, buy_count=4)
        cart.remove_product(product1, remove_count=10)
        assert product1 not in cart.products






    def test_clear(self, cart, product1):
        cart.add_product(product1, 2)

        # Очищаем корзину
        cart.clear()
        assert len(cart.products) == 0

    def test_buy_value(self , cart ):
        with pytest.raises(ValueError, match="В корзине пусто!"):
            cart.buy()


    def test_total_price(self, cart, product1 , product2):
         cart.add_product(product1, 12)
         cart.add_product(product2, 15)
         assert cart.get_total_price() == 5556

    def test_buy_value(self, cart, product1 , product2):

        cart.add_product(product1, buy_count=11)
        cart.add_product(product2 , 20)


        cart.buy()
        assert product1.quantity == 489
        assert product2.quantity == 480

        assert len(cart.products) == 0

    def test_buy_with_insufficient_stock(self, cart, product1, product2):
        """
        Проверяем, что если одного товара не хватает, второй все равно уменьшается.
        """

        cart.add_product(product1, 700)
        cart.add_product(product2, 20)

        # Покупка должна вызвать ValueError из-за недостатка товара
        with pytest.raises(ValueError, match=f"Товара '{product1.name}' недостаточно на складе!"):
            cart.buy()

        assert product1.quantity == 500
        assert product2.quantity == 500