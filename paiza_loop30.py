num = int(input())
ans = 0
for i in range(1,num+1,1):
    while i % 5 == 0:
        ans += 1
        i /= 5
print(ans)
