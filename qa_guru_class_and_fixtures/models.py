

class Product:
    """ Класс продукта """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, requested_quantity):
        """ Проверяет, достаточно ли товара в наличии для удовлетворения запроса. :param requested_quantity: Запрашиваемое количество товара :return: True, если товара достаточно, False - если недостаточно """
        return self.quantity >= requested_quantity

    def buy(self, quantity):
        """ Реализует метод покупки. Проверяет количество продукта, используя метод check_quantity. Если продуктов недостаточно, выбрасывает исключение ValueError. """
        if self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError("Недостаточно товаров на складе.")

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """ Класс корзины. В нем хранятся продукты, которые пользователь хочет купить. """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """ Метод добавления продукта в корзину. Если продукт уже есть в корзине, то увеличивается его количество. """
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count=None):
        """ Метод удаления продукта из корзины. Если remove_count не указан, то удаляется вся позиция. Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция. """
        if product in self.products:
            if remove_count is None or remove_count >= self.products[product]:
                del self.products[product]
            else:
                self.products[product] -= remove_count

    def clear(self):
        """ Полностью очищает корзину. """
        self.products.clear()

    def get_total_price(self) -> float:
        """ Возвращает общую стоимость всех товаров в корзине. """
        total_price = sum(product.price * count for product, count in self.products.items())
        return total_price

    def buy(self):
        """ Метод покупки. Учтите, что товаров может не хватать на складе. В этом случае нужно выбросить исключение ValueError. """
        for product, count in self.products.items():
            if product.check_quantity(count):
                product.buy(count)
            else:
                raise ValueError(f"Недостаточно товара '{product.name}' на складе.")