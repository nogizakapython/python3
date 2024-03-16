array1 = [1,2,5,1,4,3,2,5,1,4]
N = int(input())
count = 0
for i in list(array1):
    if i == N:
        count += 1

print(count)
