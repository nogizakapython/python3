# 残金を入力して、りんご、バナナ、オレンジの買い物をする
# 新規作成 2023/4/6

# 財布の初期値を0円にする
money = 0
# 買い物リスト
items = {'apple': 100, 'banana': 200, 'orange': 400}
# 個数変数
count = 0
while True:
    try:
        money1 = int(input("財布の金額を入力してください。但し100円以上で入力してください"))
        if money1 < 100:
            raise ValueError
        else:
            money = money1
            break
    except:
        print("金額は100円以上を入力してください")
            
for item_name in items:
    print('--------------------------------------------------')
    print('財布には' + str(money) + '円入っています')
    print(item_name + 'は1個' + str(items[item_name]) + '円です')
    while True:
        try:
            input_count = int(input('購入する' + item_name + 'の個数を入力してください：'))
            if input_count < 0:
                raise ValueError
            else:
                count = input_count
                break
        except:
            print("購入個数は0以上の整数を入力してください")
               
    print('購入する' + item_name + 'の個数は' + str(count) + '個です')
      
    total_price = items[item_name] * count
    print('支払い金額は' + str(total_price) + '円です')
    
    if money >= total_price:
        print(item_name + 'を' + str(count) + '個買いました')
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
