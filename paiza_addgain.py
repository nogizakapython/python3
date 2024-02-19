input_line = input()
array1 = input_line.split(' ')
A = int(array1[0])
B = int(array1[1])
C = int(array1[2])
zero_count = 0
if A + B + C == 0:
    zero_count += 1
if A - B + C == 0:
    zero_count += 1
if A + B - C == 0:
    zero_count += 1
if A - B - C == 0:
    zero_count += 1
if zero_count > 0:
    print("YES")
else:
    print("NO")
