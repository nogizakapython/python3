n,a,b = map(int,input().split(' '))
d = 0
array1 = []
for i in range(n):
    w_array =list(map(int,input().split(' ')))
    X = w_array[0]
    Y = w_array[1]
    array1.append([X,Y])

A = array1[a-1]
Xa = A[0]
Ya = A[1]
B = array1[b-1]
Xb = B[0]
Yb = B[1]
d = abs(Xb-Xa) + abs(Yb-Ya)
print(d)
