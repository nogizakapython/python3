# 新規作成 2023/3/22
# コンソール入力からメニュー番号を受け取ってメニューを表示する

from progate23_1 import MenuItem

menu_item1 = MenuItem('サンドイッチ', 500)
menu_item2 = MenuItem('チョコケーキ', 400)
menu_item3 = MenuItem('コーヒー', 300)
menu_item4 = MenuItem('オレンジジュース', 200)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]
ele1 = len(menu_items)

index = 0

for item in menu_items:
    print(str(index) + '. ' + item.info())
    index += 1

print('--------------------')


while True:
    # コンソールから入力を受け取り、変数 order に代入してください
    order = int(input('メニューの番号を入力してください: '))
    try:
        if order < 0 or order > ele1:
            raise ValueError
        else:
            selected_menu = menu_items[order]
            break
    except:
        print(f"0から{ele1}までの整数を入力してください")    

# 「 選択されたメニュー: 〇〇 」と出力してください
print("選択されたメニュー:" + selected_menu.name)
