# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
table0 = []
table1 = []
table2 = []
table3 = []
table4 = []
table5 = []
table6 = []
table7 = []
table8 = []
table9 = []
n = int(input())
for i in range(n):
    data = int(input())
    ans = data % 10
    if ans == 0:
        table0.append(data)
    elif ans == 1:
        table1.append(data)
    elif ans == 2:
        table2.append(data)
    elif ans == 3:
        table3.append(data)
    elif ans == 4:
        table4.append(data)    
    elif ans == 5:
        table5.append(data)
    elif ans == 6:
        table6.append(data)    
    elif ans == 7:
        table7.append(data)    
    elif ans == 8:
        table8.append(data)
    elif ans == 9:
        table9.append(data)    

table_list = [table0,table1,table2,table3,table4,table5,table6,table7,table8,table9] 

for table_name in table_list:
    e = len(table_name)
    ans = ""
    if e > 0:
        for i in range(e):
            if i == 0:
                ans += str(table_name[i])
            else:
                ans += " " + str(table_name[i])
                
    print(ans)