# 新規作成 2023/3/1
# 数値の表現
# for文を使ってn年後の福利を計算する

money = 10000
RATE = 1.08
# year = 3
print("年数を入力してください ",end="")
year = int(input())
for i in range(1,year+1):
  money *= RATE
  print(f"{i}年後の預金は{money}です")



