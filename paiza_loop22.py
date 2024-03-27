num = int(input())
data = input()
array1 = data.split(' ')
for i in array1:
    number = int(i)
    if number % 2 == 1:
        print(number)
