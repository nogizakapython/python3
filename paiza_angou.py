N = int(input())
Q = int(input())
n = [0] * Q
c = [""] * Q

for i in range(Q):
    values = input().split()
    n[i] = int(values[0]) - 1
    c[i] = values[1]

C = input()

ans = [C] * N
for i in range(Q):
    ans[n[i]] = c[i]

print("".join(ans))
