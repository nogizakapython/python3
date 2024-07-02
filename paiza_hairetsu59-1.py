n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
flag = False

for i in a:
    if i == k:
        flag = True

if flag:
    print("Yes")
else:
    print("No")
