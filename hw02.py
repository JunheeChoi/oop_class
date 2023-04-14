class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity
        self._discount_rate = 0.0

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, q):
        self._quantity = q

    @property
    def discount_rate(self):
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, value):
        self._discount_rate = value

    def get_price(self):
        return self.price * self.quantity * (1 - self.discount_rate)

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Discount Rate: {self.discount_rate}"


class ShoppingCart:
    def __init__(self):
        self.__shop_list = []

    def add(self, product):
        self.__shop_list.append(product)

    def delete(self, product, qty):
        for p in self.__shop_list:
            if p == product:
                p.quantity -= qty
                if p.quantity == 0:
                    self.__shop_list.remove(p)

    def total_price(self):
        total = 0
        for p in self.__shop_list:
            total += p.get_price()
        return total

    def billing(self):
        bill = '구입 품목:' + '\n'+'\n'
        for p in self.__shop_list:
            bill += '{:<20} {:>7}개 {:>12,}원\n'.format(p.name, p.quantity, p.get_price())
        bill += '-'*50 +'\n'
        bill += '합계{:>40,}원\n'.format(self.total_price())
        return bill


