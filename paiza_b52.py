array1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
leng1 = len(array1)
X = input()
b_num = 0
e_num = 0
c_num = 0
flag1 = 0
for i in range(leng1):
    t1 = array1[i]
    if t1 == X:
        b_num = i

Y = input()
for j in range(leng1):
    t2 = array1[j]
    if t2 == Y:
        e_num = j

C = input()
for k in range(leng1):
    t3 = array1[k]
    if t3 == C:
        c_num = k

if c_num >= b_num:
    flag1 += 1
if c_num <= e_num:
    flag1 += 1

if flag1 == 2:
    print("true")
else:
    print("false")
