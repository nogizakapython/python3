num = int(input())
guu = 0
data = input()
array1 = data.split(' ')
for i in array1:
    N = int(i)
    if N % 2 == 0:
        guu += 1

print(str(guu) + " " + str(num - guu))
