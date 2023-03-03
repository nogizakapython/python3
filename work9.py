# 新規作成 2023/3/3
# match構文を使って、BMI測定アプリを変更する

yen = 0
rate = 0.0
# 結果出力
# 出力結果関数
def output():
  separator = "=="
  print(separator * 20)

while True:
  # 例外処理
  try:
    m = int(input("金額を正の整数で入力してください "))
    yen = m
    if yen > 0:
      print("OK")
    else:
      print("正の整数で入力してください")
      raise ValueError
    break
  except:
    print("Check NG")

while True:
  # 例外処理
  try:
    R = float(input("利率を0より大きく、1より小さい小数で入力してください "))
    rate = R
    if rate > 0 and rate < 1:
      print("OK")
    else:
      print(f"利率を0より大きく、1より小さい小数で入力してください {rate:,2f}はNG")
      raise ValueError
    break
  except:
    print("Check NG")

for year in range(11):
  output()
  print(f"{year} 年後の預金額は{yen * (1+rate) ** year:,.1f}です")

