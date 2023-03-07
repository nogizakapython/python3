# リスト内包表記
# 新規作成 2023/3/7

prices = [100, 200, 150, 200, 100]

# リスト内包表記
prices_with_tax = [price * 1.1 for price in prices if price != 200]

print(prices_with_tax)
