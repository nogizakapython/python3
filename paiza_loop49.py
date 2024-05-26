num = int(input())
s_count = 0

for i in range(2,num+1):
    count = 0
    for j in range(1,i):
        if i % j == 0:
            count += 1
    if count == 1:
        s_count += 1
print(s_count)
