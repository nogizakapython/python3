# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
str1 = input()
count = 0
ans = ""
for i in str1:
    if i == "-" and count == 0:
        ans = ans + i
        count += 1
    elif i == "-" and count > 0:
        count += 1
    else:
        ans = ans + i
        count = 0


print(ans)
