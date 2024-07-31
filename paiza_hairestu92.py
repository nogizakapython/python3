num = int(input())
array1 = [int(x) for x in input().split(' ')]
count = 0
for i in range(1,num):
    for j in range(0,i):
        if array1[i] == array1[j]:
            count += 1
    if count > 0:
        print("Yes")
    else:
        print("No")
    count = 0
