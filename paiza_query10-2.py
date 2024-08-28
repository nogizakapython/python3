N, K = map(int, input().split())
names = {input() for _ in range(N)}

for _ in range(K):
    event = input()

    if event == "handshake":
        for name in sorted(names):
            print(name)
    else:
        event, name = event.split()
        if event == "join":
            names.add(name)
        else:
            names.remove(name)
