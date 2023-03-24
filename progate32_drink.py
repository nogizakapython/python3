# drinkクラス
# 新規作成2023/3/24

from progate32menu_item import MenuItem

class Drink(MenuItem):
    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.amount) + 'mL)'
