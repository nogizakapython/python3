N, X, Y = map(int, input().split())
str_s = input()
b = [0] * N
s = [0] * (N + 1)

for i in range(N):
    if str_s[i] == "b":
        b[i] = 1

for i in range(N):
    s[i + 1] = s[i] + b[i]

print(s[Y] - s[X - 1])