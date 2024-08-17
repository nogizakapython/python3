n = int(input())
s_count = 0
b_count = 0
for i in range(n):
    data = input()
    if data == "ball":
        b_count += 1
    elif data == "strike":
        s_count += 1
    if b_count == 4:
        print("fourball!")
    elif s_count == 3:
        print("out!")
    else:
        print(data + "!")
