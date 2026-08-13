# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())

for i in range(N):
    num = int(input())
    sosuu_flag = True
    if num == 1:
        sosuu_flag = False
        
    for j in range(2,int(num ** 0.5) + 1,1):
        if num % j == 0:
            sosuu_flag = False
        
    if sosuu_flag:
            print("pass")
    else:
            print("failure")