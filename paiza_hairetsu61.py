num,k = map(int,input().split(' '))
array1 = []
for i in range(num):
    data = int(input())
    array1.append(data)

for j in array1:
    print(j+k)
