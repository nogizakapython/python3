# 合格なら Yes そうでないなら No を出力してください。
N, X = list(map(int, input().split()))

for i in range(N):
    a = int(input())
    if a >= X:
        print("Yes")
    else:
        print("No")