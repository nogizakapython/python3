N,Q = map(int,input().split(' '))
array1 = [input() for _ in range(N)]
for i in range(Q):
    data1 = input()
    count = 0
    for i in range(len(array1)):
        str1 = array1[i]
        if data1 == str1 and count == 0:
            print(i+1)
            count += 1
        elif data1 == str1:
            count += 1
    if count == 0:
        print(-1)
