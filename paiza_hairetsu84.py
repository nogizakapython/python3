array1 = []
H,W,r,c = map(int,input().split(' '))
for i in range(H):
    data1 = input()
    array1.append(list(data1))

str1 = array1[r-1][c-1]
if str1 == "#":
    print("Yes")
else:
    print("No")
