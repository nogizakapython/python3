Q = int(input())

A = []  # スタック本体
for i in range(Q):
    query = input().split()
    if query[0] == "1":
        # PUSH
        A.append(query[1])
    elif query[0] == "2":
        A.pop()
    print(" ".join(A))