# 新規作成 2023/3/22
# メインモジュール

# 外部モジュールを作成する
from progate26_2 import MenuItem

menu_item1 = MenuItem('サンドイッチ', 500)
menu_item2 = MenuItem('チョコケーキ', 400)
menu_item3 = MenuItem('コーヒー', 300)
menu_item4 = MenuItem('オレンジジュース', 200)

# インスタンス配列
menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

index = 0

for item in menu_items:
    print(str(index) + '. ' + item.info())
    index += 1

print('--------------------')

order = int(input('メニューの番号を入力してください: '))
selected_menu = menu_items[order]
print('選択されたメニュー: ' + selected_menu.name)

# コンソールから入力を受け取り、変数 count に代入してください
count = int(input("個数を入力してください(3つ以上で1割引):"))

# get_total_price メソッドを呼び出してください
result = selected_menu.get_total_price(count)

# 「 合計は〇〇円です 」となるように出力してください
print("合計は" + str(result) + "円です")
