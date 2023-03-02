# 新規作成 2023/3/2
# f文字列オプション
# 複利計算プログラム

RATE = 1.1
year = 3

# 初期金額を表示する
def init(input_money):
  print(f"Year 0: {input_money:,}")


while True:
  try:
    input_money = int(input("金額を整数で円の単位で入力してください"))
    break
  except:
    print("金額は整数で円の単位で指定してください")

while True:
  try:
    year = int(input("年数を正の整数で入力してください"))
    if year < 1:
      raise Exception(year)
    else:
      break
  except:
    print("年数を整数で入力してくださいで指定してください")


init(input_money)
for i in range(1,year+1):
  input_money *= RATE
  print(f"Year {i}: {input_money:,.0f}")
