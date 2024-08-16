array1 = input().split(' ')
array2 = []
for str1 in array1:
    if str1 not in array2:
        array2.append(str1)

for a in array2:
    print(a)

for str2 in array2:
    count = 0
    for x in array1:
        if x == str2:
            count += 1
    print(count)
