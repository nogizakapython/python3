# 関数名→処理の内容→変数への代入、関数の引数
#  2023/3/6

# rateを仮引数に設定する
def double(n):
  return n * 2

def triple(n):
  return n * 3


def calc(n,func):
  # return double(10)
  return func(n)

print(calc(10,double))
print(calc(10,triple))
