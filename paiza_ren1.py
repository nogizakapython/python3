# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
array1 = []
# 入力の個数
num = 10
# 配列に10個追加
for i in range(num):
    input_line = input()
    array1.append(input_line)
# 出力文字列
str = ""
count = 0
for j in array1:
    if count < num - 1:
        str += j + " "
    elif count == num - 1:
        str += j
    count += 1
print(str)
