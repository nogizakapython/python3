num = int(input())
array1 = list(map(int,input().split(' ')))
array1.sort(reverse=False)
for i in array1:
    print(i)
