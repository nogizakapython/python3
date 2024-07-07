num = int(input())
array1 = []
for i in range(num):
    data = int(input())
    array1.append(data)

for j in range(num-1,-1,-1):
    print(array1[j])
