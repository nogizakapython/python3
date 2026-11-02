# 合格なら Yes そうでないなら No を出力してください。
N, X = list(map(int, input().split()))

for i in range(N):
    a, b = map(int,input().split())
    if a >= X and b >= X:
        print("Yes")
    else:
        print("No")