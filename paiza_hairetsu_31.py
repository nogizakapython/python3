data1 = input()
array1 = data1.split(' ')
N = int(array1[0])
data2 = int(array1[1])
data3 = input()
array2 = data3.split(' ')
count = 0
for i in list(array2):
    data4 = int(i)
    if data4 == N:
        count += 1
print(count)
