N, K = map(int, input().split())
roster = {x: y for x, y in [input().split() for _ in range(N)]}

for _ in range(K):
    s = input().split()
    if s[0] == "join":
        num, ID = s[1:]
        roster[num] = ID
    elif s[0] == "leave":
        num = s[1]
        del roster[num]
    else:
        num = s[1]
        print(roster[num])
