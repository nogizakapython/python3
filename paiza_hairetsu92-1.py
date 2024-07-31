N = int(input())
A = [int(x) for x in input().split()]

memo = {A[0]}
for i in range(1, N):
    if A[i] in memo:
        print("Yes")
    else:
        memo.add(A[i])
        print("No")
