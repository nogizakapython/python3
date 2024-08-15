array1 = input().split(" ")
array2 = []
for word in array1:
    if word not in array2:
        array2.append(word)
        print(word)
    else:
        print(1)
