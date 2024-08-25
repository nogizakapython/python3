N, K, P = map(int, input().split())
A = [int(input()) for _ in range(N)]

A.append(P)
ans = sorted(A).index(P) + 1

for _ in range(K):
    event = input()

    if event == "sorting":
        print(ans)
        continue

    x = int(event.split()[1])
    if x < P:
        ans += 1
