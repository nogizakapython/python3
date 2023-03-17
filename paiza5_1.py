# coding: utf-8
# クラスで、引数と戻り値のあるメソッドを作る

class Item:
    tax = 1.08
    def __init__(self,price,quantity):
        self.price = price
        self.quantity = quantity

    def total(self):
        return int(self.price * self.quantity * Item.tax)

apple = Item(120,15)
total = apple.total()
print(f"合計金額は{total}円です")

orange = Item(85,32)
print(f"合計金額は{orange.total()}円です")
