N, M = map(int, input().split(" "))
S = [None] * N
for i in range(N):
    S[i] = input()
print(S[M % N - 1])
