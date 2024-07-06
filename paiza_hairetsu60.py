num = int(input())
array1 = []
for i in range(num):
    data = int(input())
    array1.append(data)
array2 = list(set(array1))
print(len(array2))
