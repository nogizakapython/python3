# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
array1 = []
tagA,tagB = map(str,input().split(' '))
data = input()
data1 = data.split(tagB)
leng1 = len(data1)
for i in range(leng1):
    c = data1[i]
    cnt = 0
    ans = ""

    cleng = len(c)
    for s in c:
        if s == ">":
            cnt = 1
        if cnt == 1 and s != ">":
            ans += s

    array1.append(ans)


leng2 = len(array1)
zero_count = 0
for string1 in list(array1):
    if string1 != "":
        print(string1)
    else:
        zero_count += 1

if zero_count == leng2:
    print("<blank>")
