N,M = map(int,input().split(" "))
for i in range(M):
    data = int(input())
    flag = 0
    for j in range(1,1000):
        target1 = N * j 
        target2 = N * (j+1)
        if abs(data - target1) < abs(data - target2):
            print(target1)
            flag += 1
        if flag == 1:
            break