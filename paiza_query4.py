num = int(input())
array1 = [int(input()) for _ in range(num)]
array1.pop(0)
for i in array1:
    print(i)
