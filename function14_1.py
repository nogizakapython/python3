# 変数のスコープ
#  2023/3/6

# rateを仮引数に設定する
def get_price(a,b,c,rate):
  # 仮引数 値が代入された変数→ローカル変数
  # 値が代入されていない変数→外のスコープを探す
  # ローカル変数
  # global rate
  if a + b >= 3000:
    rate = 1.05
  total = (a + b + c) * rate
  return format(total,'.0f')

rate = 1.1
print(get_price(300,700,200,rate))
print(get_price(2000,1000,500,rate))
print(rate)

