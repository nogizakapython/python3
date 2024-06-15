data1 = input()
array1 = list(map(int,data1))
data2 = input()
array2 = list(map(int,data2))
length1 = len(array1)
ans = ""
for i in range(length1-1,-1,-1):
    calc1 = array1[i] + array2[i]
    ans = str(calc1) + ans
print(ans)
