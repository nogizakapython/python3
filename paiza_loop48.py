num = int(input())
data = input()
array1 = data.split(' ')
#print(array1)
for i in range(num):
    a = int(array1[i])
    for j in range(num):
        b = int(array1[j])
        if j < num - 1:
            print(a * b,end=' ')
        else:
            print(a * b)
