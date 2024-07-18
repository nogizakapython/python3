n = int(input())
a = [int(input()) for _ in range(n)]
ans = [None, None]
diff = 101

for i in range(n):
    for j in range(i + 1, n):
        if abs(a[i] - a[j]) < diff:
            diff = abs(a[i] - a[j])
            ans = [a[i], a[j]]

ans.sort()
for i in ans:
    print(i)
