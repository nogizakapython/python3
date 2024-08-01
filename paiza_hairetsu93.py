r_array = []
num = int(input())
array1 = [int(x) for x in input().split(' ')]
array2 = [int(x) for x in input().split(' ')]
for i in array1:
    r_array.append(i)

for j in array2:
    r_array.append(j)

r_array = list(set(r_array))
r_array.sort()


print(" ".join(map(str,r_array)))
