# リスト内包記法
# 新規作成 2023/3/7

# 配列
prices = [100, 200, 150, 200, 100]

#prices_with_tax = []

#for price in prices:
#    prices_with_tax.append(price * 1.1)

#リスト内包表記
prices_with_tax = [round(price * 1.1,0) for price in prices]

print(prices_with_tax)
