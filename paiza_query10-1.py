n,c = map(int,input().split(' '))
array1 = {input() for _ in range(n)}

for i in range(c):
    data = input()


    if data == "handshake":
        for m in sorted(array1):
            print(m)
    else:
        d,name = data.split(' ')

        if d == "join":
            array1.add(name)
        elif d == "leave":
            array1.remove(name)
