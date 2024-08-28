n,c = map(int,input().split(' '))
array1 = [ input() for _ in range(n)]
array1.sort()
for i in range(c):
    data = input()


    if data == "handshake":
        if len(array1) > 0:
            for m in array1:
                print(m)
    else:
        d,name = data.split(' ')

        if d == "join":
            array1.append(name)
        elif d == "leave":
            array1.remove(name)
    array1.sort()
