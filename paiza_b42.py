# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
array1 = ["HND", "NRT", "KIX", "NGO", "NGO", "NGO", "NGO", "NGO"]
array2 = list(set(array1))
for str1 in array2:
    count = 0
    for i in array1:
        if str1 == i:
            count += 1
    if count > 1:
        print(count)
