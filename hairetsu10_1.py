# 配列のスライス記法処理
# 新規作成 2023/3/7
# 配列をfor文でループさせて要素を表示する

prices = [100,200,150,200,100]

for index,price in enumerate(prices):
    print(f"{index}:{price * 1.1:.2f}")
