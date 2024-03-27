n = int(input())
data = input()
array1 = data.split(' ')
count = len(array1)
for i in range(count):
    number = int(array1[i])
    print(number * (i+1))
