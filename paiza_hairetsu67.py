num = int(input())
array1 = [int(input()) for _ in range(num)]
p = int(input())
array1.pop(p-1)

for k in array1:
    print(k)
