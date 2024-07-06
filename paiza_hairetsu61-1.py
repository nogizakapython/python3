n, k = map(int, input().split())
a = []

for i in range(n):
    a_i = int(input())
    a.append(a_i + k)

for i in a:
    print(i)
