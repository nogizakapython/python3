m,n = map(int,input().split(" "))
k,l = map(int,input().split(" "))
for i in range(n):
    data = int(input())
    if data < k:
        print(k)
    elif data > l:
        print(l)
    else:
        if abs(data - k ) < (l-k) /2 :
            print(k)
        else:
            print(l)