# 変数のスコープ
#  2023/3/6

def get_price(a,b):
  # 仮引数
  # ローカル変数
  total = a + b
  return total

# グローバル変数
total = 30
print(get_price(300,700))
print(total)
