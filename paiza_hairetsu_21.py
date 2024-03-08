input_line = input()
array1 = input_line.split(' ')
N = int(array1[0])
M = int(array1[1])
K = int(array1[2])
L = int(array1[3])
array1 = []
array2 = []
array3 = []
for i in range(N):
    data1 = input()
    array2 = data1.split(' ')
    data2 = ""
    for j in range(M):
        if j == M-1:
            data2 = data2 + array2[j]
        else:
            data2 = data2 + array2[j] + ","
    array3 = data2.split(",")
    array1.append(array3)


print(array1[K-1][L-1])
