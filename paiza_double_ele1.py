array1 = [[6,5,4,3,2,1],[3,1,8,8,1,3]]
N = len(array1)
for i in range(N):
    J = len(array1[i])
    for k in range(J):
        num = int(array1[i][k])
        print(num)

