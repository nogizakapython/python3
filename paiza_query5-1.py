from collections import deque

N, K = map(int, input().split())
A = deque([int(input()) for _ in range(N)])

f = 0
for _ in range(K):
    s = input()
    if s == "pop":
        A.popleft()
        continue
    for a in A:
        print(a)
