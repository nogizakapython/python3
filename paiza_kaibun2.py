str1 = input("Please input string")
array1 = []
num = len(str1)
for i in range(num):
    c = str1[i]
    array1.append(c)

ans = ""
for j in range(num-1,-1,-1):
    d = array1[j]
    ans = ans + d

if str1 == ans:
    print("YES")
else:
    print("NO")
