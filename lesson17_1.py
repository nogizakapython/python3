# 新規作成 2023/3/3
# if文を短くする

yen = 0
while True:
  try:
    i_yen = int(input("金額を整数で入力してください"))
    yen = i_yen
    if yen < 0:
      raise ValueError()
    break;
  except:
    print("文字列を入力してください");

RATE = 1.1 if yen <= 100000 else 1.05
print(f"Cuttent Rate {RATE:,.2f}")
print(f"現在の貯蓄額は{yen}です")
print(f"1年後の貯蓄額は{yen * RATE:,.1f}です")
print(f"2年後の貯蓄額は{yen * RATE * RATE:,.1f}です")
