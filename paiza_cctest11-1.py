N, X, Y = list(map(int, input().split()))
for i in range(N):
    a, b = list(map(int, input().split()))
    if X <= a and X <= b and Y <= a + b:
        print('Yes')
    else:
        print('No')