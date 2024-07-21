array1 = []
array2 = []
for i in range(4):
    w_array1 = input()
    array1.append(w_array1)


for str1 in array1:
    w_array2 = str1.split(' ')
    length1 = len(w_array2)
    for j in range(length1-1,-1,-1):
        data1 = w_array2[j]
        array2.append(int(data1))

length2 = len(array2)
array3 = []
for k in range(length2-1,-1,-1):
    data2 = array2[k]
    array3.append(data2)

target = 0
count = 1
one_count = 0
for l in array3:
    if l == 1 and one_count == 0:
        target = count
        one_count += 1
    elif l == 1:
        one_count += 1
    count += 1

print(target)
print(one_count)
