input_line = input()
array1 = input_line.split(' ')
N = int(array1[0])
M = array1[1]
data1 = input()
array2 = data1.split(' ')
hantei = M in array2
if hantei:
    print("Yes")
else:
    print("No")
