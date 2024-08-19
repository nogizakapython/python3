t,n = map(int,input().split(' '))
for _ in range(n):
    data = int(input())
    if data % t == 0:
        print("Yes")
    else:
        print("No")
