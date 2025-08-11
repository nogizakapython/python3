# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
inputstr = input()
array1 = list(inputstr)
ans = ""
for c in list(array1):
    if c == " ":
        ans = ans + "_"
    else:
        ans = ans + c
print(ans)
