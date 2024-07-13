num = int(input())
array1 = [int(input()) for _ in range(num)]

array2 = list(set(array1))

for j in array2:
    print(j)
