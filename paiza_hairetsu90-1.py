N, B = map(int, input().split())
A = {int(x) for x in input().split()}

if B in A:
    print("Yes")
else:
    print("No")
