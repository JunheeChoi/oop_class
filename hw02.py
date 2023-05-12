# Re-create class diagram by specifying whether or not to conceal attributes

# add class variable 'distance_rate'

class Product:
    discount_rate: float = 0.0
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, q):
        self.__quantity = q

    def get_price(self):
        return int(self.__price * self.__quantity * (1 - Product.discount_rate))

    def __str__(self):
        return f"{self.__name:30s}\t{self.__price:5d}원{self.__quantity:3d}개"

    @classmethod
    def change_rate(cls, rate):
        cls.discount_rate = rate

# make shop_list inaccessible outside of the object
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
        print('구입 품목\n')

        for p in self.__shop_list:
            print(f'{p}\t{p.get_price():8d}원')
        print(f'{58 * "-"}')
        print(f'{"합계":46s} {self.total_price():8d}원 ')


    def __str__(self):
        shop = ''
        for p in self.__shop_list:
            shop += f'{p}\n'

        return shop


# 2. add some products
if __name__ == "__main__":

    # create some Product instances
    p1 = Product("제주 삼다수 그린 2L", 1200, 5)
    p2 = Product("신라면(120g*5입)", 4100, 2)
    p3 = Product('CJ 햇반(210g*12입)', 13980, 1)
    p4 = Product('몽쉘크림(12입)', 4780, 1)

    # create a ShoppingCart instance
    cart = ShoppingCart()

    # add products to the cart
    cart.add(p1)
    cart.add(p2)
    cart.add(p3)
    cart.add(p4)

    # delete some quantity of a product '몽쉘크림(12입)' from the cart
    cart.delete(p4, 1)

    # add a new product to the cart
    p5 = Product('해태 구운감자(135g*5입)', 3580, 2)
    cart.add(p5)

# 4. apply 10% discount rate on all products
    Product.change_rate(0.1)

# 5. print the billing information
    print(cart.billing())
