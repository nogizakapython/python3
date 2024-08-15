array1 = input().split(" ")
array2 = []
for str1 in array1:
    if not str1 in array2:
        array2.append(str1)

for x in array2:        
    print(x)