# Food クラス
# 新規作成 2023/3/24

from progate32menu_item import MenuItem

class Food(MenuItem):
    def __init__(self, name, price, calorie):
        # super() を用いて、親クラスの __init__() を呼び出してください
        super().__init__(name,price)
        # 差分のカロリー部分を追加
        self.calorie = calorie

    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.calorie) + 'kcal)'

    def calorie_info(self):
        print(str(self.calorie) + 'kcalです')
