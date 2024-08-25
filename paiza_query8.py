N,X,P = map(int,input().split(' '))
array1 = [int(input()) for _ in range(N)]
array1.append(X)
array1.append(P)
array2 = sorted(array1)
for i in range(N):
    data = array2[i]
    if data == P:
        print(i+1)
