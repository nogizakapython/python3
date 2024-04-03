input_line = input()
array1 = input_line.split(' ')
N = int(array1[0])
M = int(array1[1])
K = int(array1[2])
count = 0
while N <= K:
    N += M
    count += 1
print(count)
