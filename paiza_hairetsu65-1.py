n = int(input())
a = [int(input()) for _ in range(n)]
b = int(input())

a.append(b)

for i in a:
    print(i)
