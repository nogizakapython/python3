num = int(input())
array1 = list(map(int,input().split(' ')))
array2 = list(map(int,input().split(' ')))
ans = ""
for i in range(num):
    a = array2[i] - array1[i]
    if i < num - 1:
        ans = ans + str(a) + " "
    else:
        ans = ans + str(a)
print(ans)
