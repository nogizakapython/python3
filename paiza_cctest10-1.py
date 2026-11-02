# 合格なら Yes そうでないなら No を出力してください。
N, X = list(map(int, input().split()))

for i in range(N):
    a, b = list(map(int, input().split()))
    if X <= a and X <= b:
        print('Yes')
    else:
        print('No')