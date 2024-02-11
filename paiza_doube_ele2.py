array1 = [[6,5,4,3,2,1],[3,1,8,8,1,3]]
N = len(array1)
ans = ""
for i in range(N):
    M = len(array1[i])
    for k in range(M):
        num = array1[i][k]
        if k == M -1:
            ans = ans + str(num)
        else:
            ans = ans + str(num) + " "
    print(ans)
    ans = ""
