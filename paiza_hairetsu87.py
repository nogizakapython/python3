array1 = []
num = int(input())
for i in range(num):
    data = input()
    array1.append(data)

array2 = list(set(array1))
array2.sort()

for str2 in array2:
    #print(str2)
    count = 0
    for str1 in array1:
        if str1 == str2:
            count += 1
    print(str2 + " " + str(count))
