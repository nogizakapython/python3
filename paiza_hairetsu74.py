num = int(input())
array1 = list(map(int,input().split(' ')))
array2 = []

for i in range(num):
    sum_p = 0
    w_array1 = list(map(int,input().split(' ')))
    for j in range(5):
        data1 = w_array1[j]
        point1 = array1[j]
        sum_p += data1 * point1
    array2.append(sum_p)


#print(array2)
print(max(array2))
