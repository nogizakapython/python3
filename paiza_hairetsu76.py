import math
x,y,z = map(int,input().split(' '))
array1= [1,x,y]
array2 = sorted(array1,reverse=True)
array3 = []
ans = z
count = 0
for i in array2:
    ans1 = math.floor(ans / i)
    if ans1 >= 1:
        count += ans1
        ans -= ans1 * i
array3.append(count)

array4 = array2[1:]
print(array4)
ans = z
count = 0
for j in array4:
    ans2 = math.floor(ans / j)
    if ans2 >= 1:
        count += ans2
        ans -= ans2 * j
array3.append(count)

print(array3)
print(min(array3))
