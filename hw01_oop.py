# 객체지향프로그래밍
## 프로그래밍 과제
# 다음은 온라인 쇼핑몰의 장바구니에 대한 클래스 다이어그램이다.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def price(self):
        return self.price * self.quantity

class ShoppingCart:
    def __init__(self):
        self.shop_list = []
    def add(self, product):
        self.shop_list.append(product)

    def delete(self, product, qty):
        for p in self.shop_list:
            if p == product:
                p.quantity -= qty
                if p.quantity == 0:
                    self.shop_list.remove(p)

    def total_price(self):
        total = 0
        for p in self.shop_list:
            total += p.price()
        return total

    