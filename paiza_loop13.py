num = int(input())
data = input()
array1 = data.split(' ')
array2 = []
for number in array1:
    array2.append(int(number))

ans = array2.index(1)
print(ans+1)
