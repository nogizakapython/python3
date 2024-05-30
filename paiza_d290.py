count = 0
for i in range(0,7):
    data = input()
    if data == "Rain":
        count += 1
if count >= 4:
    print("Yes")
else:
    print("No")
