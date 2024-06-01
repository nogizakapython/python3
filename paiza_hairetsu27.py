data1 = input()
array1 = data1.split(' ')
A = int(array1[0])
B = int(array1[1])
C = int(array1[2])
data2 = input()
array2 = list(map(int,data2.split(' ')))
tmp = array2[A-1]
array2[A-1] = array2[B-1]
array2[B-1] = tmp
for i in array2:
    print(i)
