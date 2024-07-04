count = 0
for i in range(3):
    data = int(input())
    if data >= 20:
        count += 1

if count == 3:
    print("OK")
else:
    print("NG")