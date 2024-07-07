num = int(input())
array1 = []
for i in range(num):
    data = int(input())
    array1.append(data)

x,y = map(int,input().split(' '))
tmp1 = array1[x-1]
tmp2 = array1[y-1]
array1[x-1] = tmp2
array1[y-1] = tmp1

for number in array1:
    print(number)
