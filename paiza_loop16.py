input_line = input()
array1 = input_line.split(' ')
N = int(array1[0])
M = int(array1[1])
i = 0
result = 0
while N > 0:
    ans = N % M
    result += ans * pow(10,i)
    i += 1
    N //= M
print(result)
