class ShoppingCart:
    """Класс для корзины."""

    def __init__(self):
        """Создание объекта корзины."""
        self.total = 0
        self.items = {}

    def add_item(self, item_name, quantity, price):
        """Метод добавляет товар в корзину."""
        self.total += price * quantity
        self.items.update({item_name: quantity})

    def remove_item(self, item_name, quantity, price):
        """Метод удаляет товар из корзины."""
        if item_name in self.items:
            if quantity < self.items[item_name] and quantity > 0:
                self.items[item_name] -= quantity
                self.total -= price * quantity
        elif quantity >= self.items[item_name]:
            self.total -= price * self.items[item_name]
            del self.items[item_name]

    def checkout(self, cash_paid):
        """Метод для проверки оплаты."""
        if cash_paid >= self.total:
            return cash_paid - self.total
        return 'Cash paid not enough'


class Product:
    """Класс для карточки товара."""

    all_products = []

    def __init__(self, id_code, title, description, image, price):
        """Создание объекта товара."""
        self.id = id_code
        self.title = title
        self.description = description
        self.image = image
        self.price = price
        Product.all_products.append(self)

    def __del__(self):
        """Удаление объекта товара."""
        Product.all_products.remove(self)

    # def to_dict(self):
    #     """Метод преобразовывает объект в словарь."""
    #     return dict(
    #         id=self.id,
    #         title=self.title,
    #         description=self.description,
    #         image=self.image,
    #         price=self.price
    #     )

    def from_dict(self, data):
        """Метод преобразовывает словарь в объект."""
        for field in ['title', 'description', 'image', 'price']:
            if field in data:
                setattr(self, field, data[field])
