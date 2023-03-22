# 新規作成 2023/3/22
# インスタンス変数

class MenuItem:
    def info(self,name,price):
        # 「 ○○: ¥□□ 」となるように出力してください
        self.name = name
        self.price = price
        print(self.name + ": ¥" + str(self.price))


menu_item1 = MenuItem()
menu_item1.info("サンドイッチ",300)

menu_item2 = MenuItem()
menu_item2.info("おにぎり",150)