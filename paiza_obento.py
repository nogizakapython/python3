input_line = input()
array1 = list(map(int,input_line.split(' ')))
A = array1[0]
B = int(array1[1] * 0.7)
if A >= B:
    print(B)
else:
    print(A)
