# Re-create class diagram by specifying whether or not to conceal attributes

# add an attribute 'distance_rate'

class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity
        self.discount_rate = 0.0

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

    # @property
    # def discount_rate(self):
    #     return self._discount_rate
    #
    # @discount_rate.setter
    # def discount_rate(self, value):
    #     self._discount_rate = value

    def get_price(self):
        return self.price * self.quantity * (1 - self.discount_rate)

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Discount Rate: {self.discount_rate}"

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
        bill = '구입 품목:' + '\n'+'\n'
        for p in self.__shop_list:
            bill += '{:<20} {:>7}개 {:>12,}원\n'.format(p.name, p.quantity, p.get_price())
        bill += '-'*50 +'\n'
        bill += '합계{:>40,}\n'.format(int(self.total_price()))
        return bill

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

    # print the billing information
    print(cart.billing())

# 3. delete some quantity of a product '몽쉘크림(12입)' from the cart and add the following product
    cart.delete(p4, 1)

    p5 = Product('해태 구운감자(135g*5입)', 3580, 2)

#4. apply 10% discount rate on all products



    # print the billing information again
    print(cart.billing())
