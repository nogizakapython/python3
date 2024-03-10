num1 = int(input())
data1 = input()
array1 = data1.split(' ')
num1 = int(input())
data2 = input()
array2 = data2.split(' ')
for i in array2:
    elm = int(i)
    print(array1[elm-1])
