# 新規作成 2023/3/22

class MenuItem:
    def info(self):
        # print() の中身を戻り値として返してください
        return self.name + ': ¥' + str(self.price)


menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500

# menu_item1.info() の値を出力してください
print(menu_item1.info())

menu_item2 = MenuItem()
menu_item2.name = 'チョコケーキ'
menu_item2.price = 400

# menu_item2.info() の値を出力してください
print(menu_item2.info())
