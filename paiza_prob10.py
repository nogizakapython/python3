input_line = input()
array1 = input_line.split(' ')
A = int(array1[0])
B = int(array1[1])
if A >= 10 and B < 10:
    print("YES")
else:
    print("NO")
