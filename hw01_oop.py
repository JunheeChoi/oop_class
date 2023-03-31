# 객체지향프로그래밍
## 프로그래밍 과제
# 다음은 온라인 쇼핑몰의 장바구니에 대한 클래스 다이어그램이다.
# 1. Product, ShoppingCart class 정의
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def p_price(self):
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
            total += p.p_price()
        return total

    def billing(self):
        bill = '구입 품목:' + '\n'+'\n'
        for p in self.shop_list:
            bill += '{:<20} {:>7}개 {:>12,}원\n'.format(p.name, p.quantity, p.p_price())
        bill += '-'*50 +'\n'
        bill += '합계{:>40,}원\n'.format(self.total_price())
        return bill

# 2. 정의된 Product와 ShoppingCart 클래스를 이용하여 다음과 같은 제품을 카트에 추가하는 프로그램을 작성하시오.

if __name__ == '__main__':

    p1 = Product('제주 삼다수 그린 2L', 1200, 5)
    p2 = Product('신라면(120g*5입', 4100, 2)
    p3 = Product('CJ 햇반(210g*12입)', 13980, 1)
    p4 = Product('몽쉘크림(12입)', 4780, 1)

    cart = ShoppingCart()

    cart.add(p1)
    cart.add(p2)
    cart.add(p3)

    #3.
    cart.delete(p4, 1)

    p5 = Product('해태 구운감자(135g*5입)', 3580, 2)
    cart.add(p5)

    #4.
    print(cart.billing())