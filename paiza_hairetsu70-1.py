N, n = map(int, input().split())
a = [0] * n

for i in range(N):
    a_i = input()
    if i < n:
        a[i] = a_i

for ele in a:
    print(ele)
