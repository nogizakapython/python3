num = int(input())
data1 = input()
data2 = input()
array1 = data1.split(' ')
array2 = data2.split(' ')
for i in range(0,num):
    A = int(array1[i])
    B = int(array2[i])
    print(A - B)
