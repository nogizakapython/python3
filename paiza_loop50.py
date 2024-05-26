num = int(input())
count = 0
for i in range(1,num+1):
    while True:
        if i % 2 == 0:
            count += 1
            i /= 2
        else:
            break
print(count)
