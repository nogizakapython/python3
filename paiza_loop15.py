data = input()
array1 = data.split(' ')
N = int(array1[0])
M = int(array1[1])
flag = 0
div_count = 0
while True:
    if N % M == 0:
        N /= M
        div_count += 1
    else:
        break
print(div_count)
