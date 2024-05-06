n,k = map(int,input().split(' '))
array1 = []
for i in range(n):
    data = input()
    array2 = list(map(int,data.split(' ')))
    array1.append(array2)

for j in range(n):
    print(sum(array1[j]))
