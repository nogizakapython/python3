array1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
s = input()
l = len(s)
b = s[0]
e = s[l-1]

b_num = 0
e_num = 0
for i in range(len(array1)):
    t = array1[i]
    if b == t:
        b_num = i
        break
#print(i)
for j in range(len(array1)):
    u = array1[j]
    if e == u:
        e_num = j
        break
#print(j)
if b_num < e_num:
    print("true")
else:
    print("false")
