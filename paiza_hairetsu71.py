num = int(input())
array1 = [int(input()) for _ in range(num)]
array2 = []

for i in array1:
    if i not in array2:
        array2.append(i)

for j in array2:
    print(j)
