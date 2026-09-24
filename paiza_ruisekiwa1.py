# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
#
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
sum_count = 0
array1 = [1,5,9,7,5,3,2,5,8,4]
s_array = []
for num in array1:
    sum_count += num
    s_array.append(sum_count)

print(s_array[7] - s_array[1])
