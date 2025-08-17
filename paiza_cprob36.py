# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
array1 = map(str,input().split(' '))
str2 = input()
left_count = 0
right_count = 0
leng1 = len(str2)
ans = ""
for i in range(0,leng1):
    c = str2[i]
    if c == "<":
        left_count += 1
    if c == ">":
        right_count += 1
    if left_count == 1 and right_count == 1 and c != ">":
        ans = ans + c
if ans == "":
    print("<blank>")
else:
    print(ans)
