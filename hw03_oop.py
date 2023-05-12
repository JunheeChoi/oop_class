class Product:
    rate: float = 0.0
    def __init__(self, name, regular_price, quantity):
        self.__name = name
        self.__regular_price = regular_price
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name

    @property
    def regular_price(self):
        return self.__regular_price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, q):
        self.__quantity = q

    def get_price(self):
        return int(self.__regular_price * self.__quantity * (1 - self.rate))

    def __str__(self):
        return f"{self.__name:<30s}{str(self.__quantity):<5s}\t{str(self.__regular_price):>5s}"

    @classmethod
    def change_rate(cls, rate):
        cls.rate = rate


class Sales_Product(Product):
    rate = 0.2

    def get_price(self):
        return int(self.regular_price * self.quantity * (1 - self.rate))


class Clearance_Product(Product):
    rate = 0.5

    def get_price(self):
        return int(self.regular_price * self.quantity * (1 - self.rate))


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
        print('구입 품목:\n')
        print(f'{"품목명":30s} {"수량":8s} {"정상가":10s} {"할인가":12s}')

        for p in self.__shop_list:
            print(f'{p}\t{p.get_price():>10d}  ')
        print(f'{66 * "-"}')
        print(f'{"합계":50s}\t{self.total_price():10d} ')



    def __str__(self):
        shop = ''
        for p in self.__shop_list:
            shop += f'{p}\n'

        return shop


if __name__ == "__main__":
    # 2.
    cart = ShoppingCart()
    p1 = Product('제주 삼다수 그린 2L', 1200, 5)
    p2 = Product('신라면(120g*5입)', 4100, 2)
    p3 = Sales_Product('CJ 햇반(210g*12입)', 13980, 1)
    p4 = Clearance_Product('노스페이스 올라운드 폴로 NT7PN00B', 65000, 1)

    cart.add(p1)
    cart.add(p2)
    cart.add(p3)
    cart.add(p4)

    # 3.
    print(cart.billing())




