num = int(input())
data = input()
array1 = data.split(' ')
elemcount = len(array1)
max_num = 0

for i in range(0,elemcount):
    A = int(array1[i])
    ans = A + (i+1)
    if ans >= max_num:
        max_num = ans
print(max_num)
