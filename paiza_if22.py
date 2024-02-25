input_line = input()
array1 = input_line.split(' ')
N = int(array1[0])
K = int(array1[1])
T = int(array1[2])
SUM1 = K * T
if SUM1 % N == 0:
    print("YES")
else:
    print("NO")
