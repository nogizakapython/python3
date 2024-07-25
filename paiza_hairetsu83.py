l,n = map(int,input().split(' '))
array1 = input().split(' ')
for i in range(n):
    data = input()
    if data == "1":
        array1.pop()
    elif data == "2":
        length1 = len(array1)
        for j in range(length1):
            if j == length1 - 1:
                print(array1[j],end="")
            else:
                print(array1[j],end=" ")
        print()
    else:
        a,b = map(str,data.split(' '))
        array1.append(b)
