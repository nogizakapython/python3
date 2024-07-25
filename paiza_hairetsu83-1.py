N, Q = map(int, input().split())
A = [int(x) for x in input().split()]

for _ in range(Q):
    query = [int(x) for x in input().split()]

    cmd = query[0]
    if cmd == 0:
        # push_back
        A.append(query[1])
    elif cmd == 1:
        # pop_back
        A.pop()
    else:
        # print
        print(" ".join(map(str, A)))
