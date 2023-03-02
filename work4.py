# BMI測定プログラム
# 新規作成 2023/3/2
#身長をcm単位で入力する
print("身長をcm単位で入力してください ",end="")
# 入力した文字列を変数に渡す
H = int(input())
#体重をkg単位で入力する
print("体重をkg単位で入力してください ",end="")
W = int(input())
#BMI値を計算する回数
T1 = H / 100
T2 = T1 ** 2
BMI = W / T2

print('{:.2f}'.format(BMI))
