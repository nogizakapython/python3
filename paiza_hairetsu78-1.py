n = int(input())
queue = []

for i in range(n):
    s_i = input().split()
    if s_i[0] == "in":
        queue.append(s_i[1])
    elif s_i[0] == "out" and len(queue) > 0:
        queue.pop(0)

for i in queue:
    print(i)
