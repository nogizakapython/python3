# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n,m = map(int,input().split(' '))
list1 = []
list2 = []
total = 0
for i in range(n):
    w_array = input().split(' ')
    period = int(w_array[0])
    price = int(w_array[1])
    list1.append(period)
    list2.append(price)

for j in range(1,m+1):
    w_total = 0
    count = 0
    leng1 = len(list1)
    for k in range(leng1):
        w_month = list1[k]
        w_price = list2[k]
        if j == 1:
            w_total += w_price
            count += 1
        elif w_month == 1:
            w_total += w_price
            count += 1
        elif j % w_month == 1:
            w_total += w_price
            count += 1

    if count == 2:
        w_total *= 0.9
    elif count >= 3:
        w_total *= 0.85
    total += int(w_total)

print(total)
