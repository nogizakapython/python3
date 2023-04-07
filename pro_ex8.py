# サンドイッチの購入値段を表示するプログラム
# 新規作成 2023/4/7

class MenuItem:
    # コンストラクタ
    def __init__(self,name,price):
        # 「 サンドイッチ 」の代わりに引数 name の値を代入してください
        self.name = name
        
        # 500 の代わりに引数 price の値を代入してください
        self.price = price

    def info(self):
        return self.name + ': ¥' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price


# 引数を「 サンドイッチ 」と 500 としてください
menu_item1 = MenuItem("サンドイッチ",500)

print(menu_item1.info())


count = 0
while True:
    try:
        count1 = int(input('購入個数を1以上の整数で入力してください'))
        if count1 < 1:
            raise ValueError
        else:
            count = count1
            break
    except:
        print("1以上の整数を入力してください")  
result = menu_item1.get_total_price(count)
print('合計は' + str(result) + '円です')
