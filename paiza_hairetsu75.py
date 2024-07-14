num,gp,jc = map(int,input().split(' '))
array1 = []
for i in range(num):
    data = int(input())
    if data >= gp:
        array1.append(data)
g_count = len(array1)
ans = g_count - jc
if ans < 0:
    print(0)
else:
    print(ans)
