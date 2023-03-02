# 新規作成 2023/3/2
# 文字列に値を埋め込む

fname = "Reika"
lname = "Sakurai"
age = 28
separator = "=-"
print(separator * 10)
# 数値はstr(paramater)で文字列に変換して出力する
print("I am " + fname + " " + lname + ", " + str(age) + " years old!")
print(separator * 10)

print(separator * 10)
# formatを使う
print("I am {} {}, {} years old!".format(fname,lname,age))
print(separator * 10)

print(separator * 10)
# ""の前にfを入力して文字列に値を埋め込む
print(f"I am {fname} {lname}, {age} years old!")
print(separator * 10)

