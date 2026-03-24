# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n = int(input())
count = 0
array1 = ['p','a','i','z']
for i in range(n):
    data = input()
    leng = len(data)
    for i in range(leng):
        str1 = data[i]
        for word in array1:
            if str1 == word:
                count += 1
                
    print(count)
    count = 0