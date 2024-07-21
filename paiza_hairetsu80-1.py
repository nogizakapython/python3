n, k, f = map(int, input().split())
a = [int(input()) for _ in range(k)]
a_removed = a[f:]
ans = []

for i in a_removed:
    if i not in ans:
        ans.append(i)
        print(i)
