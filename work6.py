# 新規作成 2023/3/2
# 文字列に値を埋め込む
# ユーザー関数

fname = "Reika"
lname = "Sakurai"
age = 28

# output関数の定義
def output():
  separator = "=-"
  print(separator * 10)

# 関数を呼び出す
output()
# 数値はstr(paramater)で文字列に変換して出力する
print("I am " + fname + " " + lname + ", " + str(age) + " years old!")
output()

output()
# formatを使う
print("I am {} {}, {} years old!".format(fname,lname,age))
output()

output()
# ""の前にfを入力して文字列に値を埋め込む
print(f"I am {fname} {lname}, {age} years old!")
output()

