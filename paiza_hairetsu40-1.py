N = int(input())

S = [0] * 5
values = input().split()
for i in range(5):
    S[i] = values[i]

print(S[N - 1])
