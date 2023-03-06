# 無名関数の定義
# 2の累乗を1～10まで計算する
# 新規作成 2023/3/6

def s(a,func):
  return func(a)

num = 0
while True:
  try:
    num1 = int(input("自然数を入力してください"))
    if num1 < 1:
      raise ValueError
    else:
      num = num1
      break
  except:
    print("1以上の整数ではありません")

for i in range(1,num+1):
  res = s(2,lambda a:a**i)
  print(f"2の{i}乗は{res}である")

