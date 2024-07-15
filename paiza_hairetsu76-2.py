import math
x,y,z = map(int,input().split(' '))
array1= [1,x,y]
array2 = sorted(array1,reverse=True)
array3 = []

def answer(w_array,ans):
    count = 0
    for i in w_array:
        ans1 = math.floor(ans / i)
        if ans >= 1:
            count += ans1
            ans -= ans1 * i
    return count

ans = z
count1 = answer(array2,ans)
array3.append(count1)

array4 = array2[1:]
count1 = answer(array4,ans)
array3.append(count1)


print(min(array3))
