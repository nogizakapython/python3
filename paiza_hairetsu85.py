array1 = [0,1,2,3,4,5,6,7,8,9]
count = 0

num1 = int(input())
w_array = list(map(int,input().split(' ')))
length1 = len(array1)
for i in range(length1):
    count = 0
    d = array1[i]
    for j in w_array:
        if j == d:
            count += 1
    if d < length1 - 1:
        print(count,end=' ')
    else:
        print(count,end='')
