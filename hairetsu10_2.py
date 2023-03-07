# 配列のスライス記法処理
# 新規作成 2023/3/7
# 配列をfor文でループさせて要素を表示する

prices = [100,200,150,200,100]
prices2 = []

for index,price in enumerate(prices):
    prices2.append(round(price * 1.1,0))

for index1,price in enumerate(prices2):
    print(f"{index} : {price}")
