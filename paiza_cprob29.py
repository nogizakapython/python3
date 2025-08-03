# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
num = int(input())
flag1 = 0
syo = num
ans = ""
one_count = 0
while flag1 == 0:
    amari = int(syo % 2)
    syo = int(syo / 2)

    ans = ans + str(amari)

    if syo == 0:
        flag1 = 1

leng1 = len(ans)

for i in range(0,leng1):
    data = ans[i]
    if data== "1":
        one_count += 1
print(one_count)
