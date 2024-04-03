input_line = input()
array1 = input_line.split(' ')
A = int(array1[0])
B = int(array1[1])
count = 0
while A <= B:
    A += int(A * 0.1)
    count += 1
print(count)
