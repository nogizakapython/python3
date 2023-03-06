# lambdaで無名関数を作る
#  2023/3/6

# rateを仮引数に設定する
# def double(n):
#   return n * 2

# def triple(n):
#   return n * 3


def calc(n,func):
  # return double(10)
  return func(n)

# print(calc(10,double))
# 無名関数
print(calc(10,lambda n:n*2))
# print(calc(10,triple))
# 無名関数
print(calc(10,lambda n:n*3))
