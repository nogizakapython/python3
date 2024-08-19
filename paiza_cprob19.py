t,n = map(int,input().split(' '))
for i in range(n):
    data = int(input())
    w_ans = int(data / t)
    w_amari = int(data % t)
    if w_ans == 0:
        print(t)
    elif w_ans > 0 and w_amari < t/2:
        print(w_ans * t)
    else:
        print((w_ans+1) * t)
