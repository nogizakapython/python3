N,K,P = map(int,input().split(' '))
A = [int(input()) for _ in range(N)]
A.append(P)
for num in range(K):
    B = input().split(' ')
    leng1 = len(B)
    if leng1 == 2:
        A.append(int(B[1]))
    else:
        A.sort()
        for i in range(len(A)):
            data = A[i]
            if data == P:
                print(i+1)
