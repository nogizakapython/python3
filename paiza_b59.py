n,m = map(int,input().split(' '))
array1 = []
for i in range(n):
    array1.append(input())
data = input()
for j in range(len(array1)):
    target = array1[j]
    if target == data:
        print(j+1)
