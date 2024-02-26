data = input()
array1 = data.split(' ')
N = int(array1[0])
K = int(array1[1])
T = int(array1[2])
if N * K <= T:
    print("YES")
else:
    print("NO")
