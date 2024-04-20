input_line = input()
array1 = list(map(int,input_line.split(' ')))
A = array1[0]
B = array1[1]
array2 = []
for i in range(A):
    data = input()
    data_array1 = data.split(' ')
    array2.append(data_array1)
for i in range(A):
    for j in range(B):
        data1 = int(array2[i][j])
        if data1 == 1:
            print(str(i+1) + " " + str(j+1))
            break
