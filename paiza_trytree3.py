# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください

import re

n = int(input())
array1 = []

for i in range(n):
    data = input()
    array1.append(data)
    
target = input()
m = len(target)

for i in range(n):
    str1 = array1[i]
    if str1 == target:
        print("#")
    else:    
        result = re.search(target,str1)
        if result:
            print(str1[m])
        else:
            print("/")
