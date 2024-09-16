array1 = ["HND", "NRT", "KIX", "NGO", "NGO"]
array2 = list(set(array1))
count = 0
chech = 0
for i in range(len(array2)):
    count = 0
    for j in range(len(array1)):
        if array2[i] == array1[j]:
            count += 1
    if count > 1:
        check = 1

if check > 0:
    print("true")
else:
    print("false")
