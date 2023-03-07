# for文の中にif文を入れて200の要素のみ処理から外す
# 新規作成 2023/3/7

prices = [100, 200, 150, 200, 100]

prices_with_tax = []

for price in prices:
    if price != 200:
        prices_with_tax.append(price * 1.1)


print(prices_with_tax)
