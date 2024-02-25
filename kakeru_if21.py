data = input()
array1 = data.split(' ')
A = int(array1[0])
B = int(array1[1])
kakeru_count = 0
while A < B:
    A *= 2
    kakeru_count += 1
print(kakeru_count)
