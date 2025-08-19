# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
str1 = input()
str2 = input()
count = 0
s_start = 0
e_start = 0
lengstr = len(str2)

for i in range(lengstr):
    c = str2[i]
    if c == "<":
        count += 1
        if count % 2 == 0:
            e_start = i + 1
            print(str(s_start) + " " + str(e_start))
        else:
            s_start = i + 1
