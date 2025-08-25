N, M = map(int, input().split(' '))
sum = 0
for i in range(0, N):
    A = int(input())
    sum += A

if sum <= M:
    print("OK")
else:
    print("NG")
