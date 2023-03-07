# 新規作成 2023/3/7
# 配列の最大、最小、平均、並び替え

scores = [30,20,70,40,10,50]
num = 0
pot = 0


while True:
  try:
    num1 = int(input("整数を1つ入力してください"))
    num = num1
    break
  except:
    print("整数を入力してください")

# 配列を1つ追加
scores.append(num1)

while True:
  try:
    w_n = len(scores)
    num2 = int(input(f"0から{w_n}までの整数を1つ入力してください"))
    if num2 < 0 or num2 > w_n:
      raise ValueError
    pot = num2
    break
  except:
    print("整数を入力してください")
# 配列の要素を1つ削除
scores.pop(pot)
print(scores)
print(max(scores))
print(min(scores))
print(sum(scores))
avg1 = round(sum(scores) / len(scores),1)
print(avg1)
