import math

num = int(input())
data = input()
array1 = data.split(' ')
array1_count = len(array1)
array2 = []
for i in range(array1_count):
    input_value = int(array1[i])
    array2.append(input_value)

total_value = float(sum(array2))
max_value = float(max(array2))
min_value = float(min(array2))
avg_count = array1_count - 2
avg = float(total_value - max_value - min_value)
ans = float(avg / avg_count)
ans = math.floor(ans * 10) / 10
print(ans)
