money = 1000
items = {'apple': 100, 'banana': 200, 'orange': 400}
for item_name in items:
    print('--------------------------------------------------')
    print('財布には' + str(money) + '円入っています')
    print(item_name + 'は1個' + str(items[item_name]) + '円です')
    
    input_count = input('購入する' + item_name + 'の個数を入力してください：')
    print('購入する' + item_name + 'の個数は' + input_count + '個です')
    
    count = int(input_count)
    total_price = items[item_name] * count
    print('支払い金額は' + str(total_price) + '円です')
    
    if money >= total_price:
        print(item_name + 'を' + input_count + '個買いました')
        money -= total_price
        # if 文を用いて、 money の値が 0 のときの条件を分岐してください
        if money == 0:
          print("財布が空になりました")
        
        
    else:
        print('お金が足りません')
        print(item_name + 'を買えませんでした')
        break
# 変数 money と型変換を用いて、「 残金は◯◯円です 」となるように出力してください
print("残金は"+ str(money) + "円です")
