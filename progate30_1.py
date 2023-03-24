# 新規作成 2023/3/24
# 継承したクラスのオーバーライド

from progate30_food import Food
from progate30_drink import Drink

food1 = Food('サンドイッチ', 500)
food1.calorie = 330

# food1 に対して info メソッドを呼び出して戻り値を出力してください
print(food1.info())

drink1 = Drink('コーヒー',300)
drink1.amount = 300

print(drink1.info())
