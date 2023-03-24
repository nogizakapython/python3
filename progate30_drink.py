# drinkクラス
# 新規作成2023/3/24

from progate30menu_item import MenuItem

class Drink(MenuItem):
    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.amount) + 'mL)'
