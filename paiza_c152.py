num = int(input())
data1 = input()
array1 = data1.split(' ')
ar1_len = len(array1)
array2 = []
for i in range(ar1_len-1):
    data2 = array1[i]
    data3 = array1[i+1]
    if data2 == "2" and data3 == "0":
        array2.append(i+1)

ar2_len = len(array2)
ans = ""
if ar2_len == 0:
    ans = ans + "-1"
else:
    for j in range(ar2_len):
        if j == ar2_len-1:
            ans = ans + str(array2[j])
        else:
            ans = ans + str(array2[j]) + " "
print(ans)
