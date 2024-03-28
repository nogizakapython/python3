input_line = input()
array1 = input_line.split(' ')
N = int(array1[0])
A = int(array1[1])
B = int(array1[2])
data = input()
array2 = data.split(' ')
sum1 = 0
count = len(array2)
for i in range(A-1,B):
    number = int(array2[i])
    sum1 += number
print(sum1)
