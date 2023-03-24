# 新規作成 2023/3/24


from progate33_food import Food
from progate33_drink import Drink

food1 = Food('サンドイッチ', 500, 330)
food2 = Food('チョコケーキ', 400, 450)
food3 = Food('シュークリーム', 200, 180)

foods = [food1, food2, food3]

drink1 = Drink('コーヒー', 300, 180)
drink2 = Drink('オレンジジュース', 200, 350)
drink3 = Drink('エスプレッソ', 300, 30)

drinks = [drink1, drink2, drink3]

print('食べ物メニュー')
index = 0
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1

print('飲み物メニュー')
index = 0
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index += 1

print('--------------------')

food_order = int(input('食べ物の番号を選択してください: '))
selected_food = foods[food_order]

drink_order = int(input('飲み物の番号を選択してください: '))
selected_drink = drinks[drink_order]

# コンソールから入力を受け取り、変数 count に代入してください
count = int(input("何セット買いますか？(3つ以上で1割引): "))

# selected_food と selected_drink のそれぞれに対して、 get_total_price メソッドを呼び出してください
result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

# 「 合計は〇〇円です 」となるように出力してください
print("合計は" + str(result) + "円です")
