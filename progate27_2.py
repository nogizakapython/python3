# 新規作成 2023/3/22
# MenuItemクラスの共通メソッドモジュール

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': ¥' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        
        # count が 3 以上のとき、 total_price に 0.9 をかけてください
        if count >= 3:
          total_price *= 0.9
        
        # total_price を四捨五入して、 return してください
        return round(total_price)
