num = int(input())
array1 = []
array1.append(0)
array1.append(1)
if num >= 2:
    for i in range(2,num+1):
        a = array1[i-2]
        b = array1[i-1]
        array1.append(a+b)

for j in range(num):
    print(array1[j])
