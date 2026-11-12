# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
h,w,k = map(int,input().split())
h_l = h + k
w_l = w + k
array1 = []

flag1 = False
ans = ""
elem = 0

for p in range(h):
    data = input()
    array1.append(data)

for i in range(h_l + k):
    if i >= k and i <= h_l - 1:
        flag1 = True
    for j in range(w_l + k):  
          if flag1:
              str1 = array1[elem]
              if j >= k and j <= w_l - 1:
                  
                  ch = str1[j - k]
                  ans += ch
                      
              else:
                  ans += "#"
          else:
              ans += "#"
    print(ans)
    if flag1:
        elem += 1
    
    flag1 = False
    ans = ""
    
