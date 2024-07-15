import math
x,y,z = map(int,input().split(' '))
array1= [1,x,y]
array2 = sorted(array1,reverse=True)
count = 0
for i in array2:
    ans = math.floor(z / i)
    if ans >= 1:
        count += ans
        z -= ans * i
    print(ans)
    print(z)

print(count)
