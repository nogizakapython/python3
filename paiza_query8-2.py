N,X,P = map(int,input().split(' '))
array1 = [int(input()) for _ in range(N)]
array1.append(X)
array1.append(P)
array1.sort()
print(array1)
for i in range(len(array1)):
    data = array1[i]
    if data == P:
        print(i+1)
