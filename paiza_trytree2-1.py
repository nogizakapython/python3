N = int(input())
A = set()
for i in range(N):
    S = input()
    prefix = ""
    for j in S:
        prefix += j
        A.add(prefix)

ans = sorted(A)

for i in ans:
    print(i)