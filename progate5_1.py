# 新規作成　2023/3/8
# 辞書配列から要素を取り出し、キーと値から購入する個数を入力し、結果を出力する

items = {'apple': 100, 'banana': 200, 'orange': 400}
for item_name in items:
    print('--------------------------------------------------')
    print(item_name + 'は1個' + str(items[item_name]) + '円です')
    
    # input を用いて入力を受け取り、変数 input_count に代入してください
    
    input_count = input("購入する" + item_name + "の個数を入力してください：")
    # キーと変数 input_count を用いて「 購入する◯◯の個数は△△個です 」となるように出力してください
    print("購入する" + item_name + "の個数は" + input_count + "個です")
    
    # input_count を数値として変数 count に代入してください
    count = int(input_count)
    # 変数 total_price に果物1個の値段と変数 count を掛けた値を代入してください
    total_price = items[item_name] * count
    # 変数 total_price と型変換を用いて、「 支払い金額は◯◯円です 」となるように出力してください
    print("支払い金額は" + str(total_price) + "円です")