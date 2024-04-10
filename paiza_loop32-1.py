num = int(input())
data = input()
array1 = data.split(' ')
elemcount = len(array1)
min_num = 9999999

for i in range(0,elemcount):
    A = int(array1[i])
    ans = A + (i+1)
    if ans < min_num:
        min_num = ans
print(min_num)
