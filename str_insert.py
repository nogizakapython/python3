str1 = input()
num = len(str1)
array1 = []
for i in range(num):
    c =  str1[i]
    array1.append(c)
data = input()
array2 = data.split(' ')
j = int(array2[0])
char1 = array2[1]
array1[j-1] = char1
ans = ""
for k in array1:
    ans = ans + k

print(ans)
