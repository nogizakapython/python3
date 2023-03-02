# 新規作成 2023/3/2
# BMI測定及び肥満度判定

height = 0
weight = 0.0
# 結果出力
# 出力結果関数
def output():
  separator = "=="
  print(separator * 20)

# 肥満度判定関数
def hantei(data):
  if data < 18.5:
    print("痩せ過ぎです")
  elif data < 25:
    print("普通体重です")
  elif data < 30:
    print("軽程度肥満です")
  elif data < 35:
    print("中程度肥満です")
  else:
    print("高程度の肥満です")

# 標準体重計算関数
def calc_sweight(w_h):
  # 小数点以下1位まで求める
  r = format(w_h * 22,'.1f')
  # 結果を返す
  return r

while True:
  # 例外処理
  try:
    H = int(input("身長をcm単位で整数で入力してください "))
    height = H
    break
  except:
    print("Check NG")

while True:
  # 例外処理
  try:
    W = float(input("体重をkg単位で整数または小数で入力してください "))
    weight = W
    break
  except:
    print("Check NG")

# BMIの値を計算する
w_h = (height / 100) ** 2
BMI = weight / w_h
# 結果を出力する
output()
print("あなたのBMIの値は{:.2f}です".format(BMI))
# 肥満度を表示する
hantei(BMI)
# 標準体重を計算する
result =  calc_sweight(w_h)
print(f"標準体重は{result}kgです")
output()

