array1 = input().split(' ')
array2 = []
for i in array1:
    if not i in array2:
        print(i)
        array2.append(i)
    else:
        print("already_been")