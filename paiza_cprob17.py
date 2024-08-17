n = int(input())
s_count = 0
for i in range(n):
    data = input()
    if data == "strike":
        s_count += 1
        print(data + "!")
        print(s_count)
    else:
        print(data)
