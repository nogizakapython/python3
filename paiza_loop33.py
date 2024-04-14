num = int(input())
data = input()
array1 = data.split(' ')
elem_count = len(array1)
for i in range(elem_count):
    num = int(array1[i])
    if num == 1:
        print(i+1)
