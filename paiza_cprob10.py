array1 = input().split(' ')
array2 = []
for x in array1:
    if x not in array2:
        array2.append(x)

for y in array2:
    count = 0
    for z in array1:
        if z == y:
            count += 1
    print(y + " " + str(count))
