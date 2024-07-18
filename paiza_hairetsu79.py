num = int(input())
array1 = []
array2 = []
for i in range(num):
    data = int(input())
    array1.append(data)
sub = 101

array1.sort()
sa1 = 0
sa2 = 0
for j in range(num-1):
    data1 = array1[j]
    data2 = array1[j+1]
    if data2 - data1 < sub:
        sub = data2 - data1
        sa1 = data1
        sa2 = data2

array2.append(sa1)
array2.append(sa2)

for ans in array2:
    print(ans)
