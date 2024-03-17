input_line = input()
array1 = input_line.split(' ')
A = int(array1[0])
B = int(array1[1])
point = A - B
if point < 0:
    point = 0

print(point)
