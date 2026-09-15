import queue

Q = int(input())

q1 = queue.Queue()
q2 = queue.Queue()  # キュー本体
for i in range(Q):
    query = input().split()
    if query[0] == "1":
        if query[1] == "1":
            q1.put(query[2])
        else:
            q2.put(query[2])
    elif query[0] == "2":
        if query[1] == "1":
            print(q1.get())
        else:
            print(q2.get())
    else:
        print(q1.qsize(), q2.qsize())