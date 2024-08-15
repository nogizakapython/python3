array1 = input().split(" ")
array2 = []
for i in array1:
    if not i in array2:
        array2.append(i)
        
count = 0
for ch in array2:
    for data in array1:
        if data == ch:
            count += 1 
    print(ch + " " + str(count))
    count = 0