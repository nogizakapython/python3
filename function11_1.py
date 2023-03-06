# 変数のスコープ
#  2023/3/6

def get_price(a,b):
  # 仮引数 値が代入された変数→ローカル変数
  # 値が代入されていない変数→外のスコープを探す
  # ローカル変数
  total = (a + b) * rate
  return format(total,'.0f')

rate = 1.1
print(get_price(300,700))

