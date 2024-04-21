array1 = list(map(int,input().split(' ')))
A = array1[0]
B = array1[1]
array2 = []
for i in range(A):
    data = input()
    array2.append(list(map(int,data.split(' '))))
max_value = 0
for j in range(A):
    for k in range(B):
        if array2[k][j] >= max_value:
            max_value = array2[k][j]

print(max_value)
