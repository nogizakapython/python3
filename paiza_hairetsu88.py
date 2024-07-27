N,M = map(int,input().split(' '))
d = {}
for i in range(N):
    key,value = map(str,input().split(' '))
    d[key] = int(value)

for j in range(M):
    data = input()
    if data in d:
        print(d[data])
    else:
        print(-1)
