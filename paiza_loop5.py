num = int(input())
data = input()
array1 = data.split(' ')
leng = len(array1)
for i in range(0,leng):
    number = int(array1[i])
    print(number * 2)
