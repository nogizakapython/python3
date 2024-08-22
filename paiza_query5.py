m,c = map(int,input().split(' '))
array1 = [ int(input()) for _ in range(m)]
for i in range(c):
    data = input()
    length1 = len(array1)
    if length1 > 0:
        if data == "pop":
            array1.pop(0)
        elif data == "show":
            for j in array1:
                print(j)

