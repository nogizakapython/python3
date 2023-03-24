# Food クラス
# 新規作成 2023/3/24

from progate30menu_item import MenuItem

class Food(MenuItem):
    # info メソッドを定義してください
    def info(self):
      return self.name + ': ¥' + str(self.price) + ' (' + str(self.calorie) + 'kcal)'


    def calorie_info(self):
        print(str(self.calorie) + 'kcalです')
