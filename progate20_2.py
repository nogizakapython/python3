# 新規作成 2023/3/22
# インスタンス変数

class MenuItem:
    def info(self):
        # 「 ○○: ¥□□ 」となるように出力してください
        print(self.name + ": ¥" + str(self.price))


menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500

menu_item1.info()

menu_item2 = MenuItem()
menu_item2.name = 'チョコケーキ'
menu_item2.price = 400

menu_item2.info()