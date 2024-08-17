n = int(input())
s_count = 0
for i in range(n):
    data = input()
    if data == "strike":
        s_count += 1
    if s_count == 3:
        print("out!")
    elif data == "strike":
        print(data + "!")
    else:
        print(data)
