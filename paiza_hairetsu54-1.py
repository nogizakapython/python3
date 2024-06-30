N = int(input())

fibo = [0] * N
fibo[0] = 0
fibo[1] = 1

for i in range(2, N):
    fibo[i] = fibo[i - 2] + fibo[i - 1]

for ele in fibo:
    print(ele)
