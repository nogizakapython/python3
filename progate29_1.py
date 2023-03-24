# 新規作成 2023/3/24
# 継承したクラスのオーバーライド

from progate29_food import Food
from progate29_drink import Drink

food1 = Food('サンドイッチ', 500)
food1.calorie = 330

# food1 に対して info メソッドを呼び出して戻り値を出力してください
print(food1.info())
