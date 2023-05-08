# 新規作成 2023/4/6
# 単かと合計額を表示するプログラム

class MenuItem:
    def info(self):
        return self.name + ': ¥' + str(self.price)

    # get_total_price メソッドを定義してください
    def get_total_price(self,count):
      total_price = self.price * count
      return total_price


menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500

print(menu_item1.info())

count = 0
while True:
    try:
        count1 = int(input("購入する個数を入力してください"))
        if count1 < 1:
            raise ValueError
        else:
            count = count1
            break   
    except:
        print("個数は1以上の整数を入力してください")
            
# get_total_price メソッドを呼び出してください
result = menu_item1.get_total_price(count)

# 「 合計は〇〇円です 」となるように出力してください
print("合計は" + str(result) + "円です")
