num = int(input())
data = input()
array1 = data.split(' ')
sum1 = 0
for i in array1:
    data1 = int(i)
    if data1 % 2 == 1:
        break
    else:
        sum1 += data1
print(sum1)
