Q = int(input())

A = []  # キュー, スタック本体
for i in range(Q):
    query = input().split()
    if query[0] == "1":
        # PUSH
        A.append(query[1])
    elif query[0] == "2":
        # STAY(何もしない)
        continue
print(len(A))
for i in range(len(A)):
    print(A[i])