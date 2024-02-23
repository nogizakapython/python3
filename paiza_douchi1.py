num = int(input())
data1 = input()
array1 = data1.split(' ')
data2 = input()
array2 = data2.split(' ')
count = 0
for i in range(num):
    if array1[i] == array2[i]:
        count += 1
print(count)
