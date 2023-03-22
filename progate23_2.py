# 新規作成 2023/3/22

# MenuItem クラスのコードを貼り付けてください
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': ¥' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price

