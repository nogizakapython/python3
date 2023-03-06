# 変数のスコープ
#  2023/3/6

def get_price(a,b,c):
  # 仮引数 値が代入された変数→ローカル変数
  # 値が代入されていない変数→外のスコープを探す
  # ローカル変数
  rate = 1.08
  if a + b >= 3000:
    rate = 1.05
  total = (a + b + c) * rate
  return format(total,'.0f')

# rate = 1.08
print(get_price(3000,7000,2000))

